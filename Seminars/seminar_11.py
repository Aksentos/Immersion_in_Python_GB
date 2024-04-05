'''Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''
import time

class MySrting(str):
    def __new__(cls, value, author = None):
        instance = super().__new__(cls, value)
        instance.name = value
        instance.author = author
        instance.time = time.time()

        return instance


st = MySrting('slovo', 'Jon')
print(f'{st = }\n{st.author = }\n{st.time = }')

"""Задание №2 + Задание №3 + Задание №4
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
"""


# var 1
class Archive:
    """Этот класс создает объекты и сохраняет их в архив data"""

    data = []

    def __new__(cls, *args):
        instance = super().__new__(cls)
        instance.num = args[0]
        instance.string = args[1]
        instance.data = cls.data.copy()
        cls.data.append(instance)
        return instance

    def __str__(self) -> str:
        return f"STR: {self.num} {self.string}"

    def __repr__(self) -> str:
        return f"REPR: {[self.num, self.string]}"


a = Archive(1, "asd")
b = Archive(2, "ghj")
c = Archive(3, "zxc")

print(f"{a}\n{b}\n{c}")
print(f"{a = }\n{b = }\n{c = }")

"""Задание №5 + Задание №6
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""
# from functools import total_ordering


# @total_ordering
class Rectangle:
    """Класс создает объект - прямоугольники"""

    def __init__(self, length, width=0) -> None:
        self.length = length
        self.width = width if width else length

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
rec2 = Rectangle(5)
rec3 = Rectangle(10, 6)

print(rec - rec2)
print(rec + rec2)
print(rec * 5)
print(rec == rec2)
print(rec < rec2)
print(rec <= rec3)
