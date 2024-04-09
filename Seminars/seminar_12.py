"""Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""


class Factorial:
    def __init__(self, k: int) -> None:
        self.k = k
        self._history = []

    def __call__(self, value):
        result = 1
        for i in range(1, value + 1):
            result *= i
        self._history.append((value, result))
        self._history = self._history[-self.k :]
        return result

    @property
    def history(self):
        return self._history


num = Factorial(2)
print(num(3))
print(num(5))
print(num(7))
print(num(2))
print(num.history)

"""Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
import json


class Factorial:
    def __init__(self, k: int) -> None:
        self.k = k
        self._history = []

    def __call__(self, value):
        result = 1
        for i in range(1, value + 1):
            result *= i
        self._history.append((value, result))
        self._history = self._history[-self.k :]
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("result.json", "a", encoding="utf-8") as file:
            json.dump(self._history, file)

    @property
    def history(self):
        return self._history


num = Factorial(2)
with num as jsfile:
    print(num(2))
    print(num(4))
    print(num(5))
    print(num(1))

"""
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class FactorialGenerator:
    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.start = 1
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]

    def factorial(self):
        result = 1
        for i in range(self.start, self.stop + 1, self.step):
            result *= i
        return result
## ДОДЕЛАТЬ!!! не совсем работает)
    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     self.start += self.step
    #     while self.start <= self.stop:
    #         return self.factorial()
    #     raise StopIteration


num = FactorialGenerator(5)
print(num.factorial())

for n in num:
    print(n)


"""Задание №4 + Задание №5
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""


class Rectangle:
    """Класс создает объект - прямоугольники"""

    __slots__ = ("_length", "_width")

    def __init__(self, length, width=0) -> None:
        self._length = length
        self._width = width if width else length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            print("Значение должно быть больше 0!")

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Значение должно быть больше 0!")

    def perimeter(self):
        """Вычисление периметра прямоугольнка"""
        return 2 * (self.width + self.length)

    def area(self):
        """Вычисление площади прямоугольнка"""
        return self.width * self.length

    def __add__(self, other):
        """Сложение сторон двух прямоугольников"""
        if isinstance(other, Rectangle):
            new_length = self.length + other.length
            new_width = self.width + other.width
            return Rectangle(new_length, new_width)
        raise ValueError("Ошибка класса")

    def __sub__(self, other):
        """Вычитание сторон двух прямоугольников"""
        if isinstance(other, Rectangle):
            if self.length > other.length and self.width > other.width:
                return Rectangle(self.length - other.length, self.width - other.width)
            raise ValueError("Неверное соотношение сторон")
        raise ValueError("Ошибка класса")

    def __mul__(self, other):
        """Умножение сторон прямоугольнка на число"""
        if isinstance(other, (int, float)):
            return Rectangle(self.length * other, self.width * other)

    def __str__(self) -> str:
        return f"length = {self.length} width = {self.width}"

    def __eq__(self, other):
        """Сравнение площадей двух прямоугольников на равенство"""
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        raise ValueError("Ошибка класса")

    def __gt__(self, other):
        """Сравнение площадей двух прямоугольников (первый больше второго)"""
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        raise ValueError("Ошибка класса")

    def __ge__(self, other):
        """Сравнение площадей двух прямоугольников (первый не больше второго)"""
        if isinstance(other, Rectangle):
            return self.area() <= other.area()
        raise ValueError("Ошибка класса")


rec = Rectangle(6, 10)


print(rec.length)
rec.length = 10
print(rec.length)
print(rec.__slots__)
rec.color = "red"  # AttributeError: 'Rectangle' object has no attribute 'color'


"""Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Valid:

    def __init__(self, min_value: float = None, max_value: float = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{value} is lesser than {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{value} is greater than {self.max_value}")


class Rectangle:
    width = Valid(1, 100)
    length = Valid(1, 200)

    def __init__(self, width: float, length: float = None) -> None:
        self.width = width
        self.length = length if length else width

