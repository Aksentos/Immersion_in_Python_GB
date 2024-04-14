'''Исключение NegativeValueError
Добавьте в задачу Rectangle, которую писали ранее, исключение 
NegativeValueError, которое выбрасывается при некорректных значениях 
ширины и высоты, как при создании объекта, так и при установке их через сеттеры.
'''
class NegativeValueError(Exception):
    """NegativeValueError обработка неверного значения"""

    def __init__(self, text, value) -> None:
        self.text = text
        self.value = value

    def __str__(self) -> str:
        return f"{self.text} должна быть положительной, а не {self.value}"


class Rectangle:
    """Класс создает объект - прямоугольник"""

    def __init__(self, width, height=None) -> None:
        if isinstance(width, (int, float)) and width > 0:
            self.width = width
        else:
            raise NegativeValueError("Ширина", width)
        # self.height = height if height else width
        if height is None:
            self.height = width
        elif isinstance(height, (int, float)) and height > 0:
            self.height = height
        else:
            raise NegativeValueError("Высота", height)

    def __setattr__(self, __name: str, __value: float) -> None:
        if isinstance(__value, (int, float)) and __value > 0:
            return object.__setattr__(self, __name, __value)
        else:
            if __name == "width":
                raise NegativeValueError("Ширина", __value)
            elif __name == "height":
                raise NegativeValueError("Высота", __value)

    def perimeter(self):
        """Вычисление периметра прямоугольнка"""
        return 2 * (self.height + self.width)

    def area(self):
        """Вычисление площади прямоугольнка"""
        return self.height * self.width

    def __add__(self, other):
        """Сложение сторон двух прямоугольников"""
        if isinstance(other, Rectangle):
            new_width = self.width + other.width
            new_height = self.height + other.height
            return Rectangle(new_width, new_height)
        raise ValueError("Ошибка класса")

    def __sub__(self, other):
        """Вычитание сторон двух прямоугольников"""
        if isinstance(other, Rectangle):
            if self.width > other.width and self.height > other.height:
                return Rectangle(self.width - other.width, self.height - other.height)
            raise ValueError("Неверное соотношение сторон")
        raise ValueError("Ошибка класса")

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
        """Сравнение площадей двух прямоугольников (первый не меньше второго)"""
        if isinstance(other, Rectangle):
            return self.area() >= other.area()
        raise ValueError("Ошибка класса")

    def __str__(self) -> str:
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"


# test 1
r = Rectangle(-2)
"""
Ожидаемый ответ:
__main__.NegativeValueError: Ширина должна быть положительной, а не -2
"""

# test 2
r = Rectangle(5, -3)
"""
Ожидаемый ответ:
__main__.NegativeValueError: Высота должна быть положительной, а не -3
"""

# test 3
r = Rectangle(4, 4)
r.width = -3

"""
Ожидаемый ответ:
__main__.NegativeValueError: Ширина должна быть положительной, а не -3
"""

# test 4
r = Rectangle(4, 4)
r.height = -3

"""
Ожидаемый ответ:
__main__.NegativeValueError: Высота должна быть положительной, а не -3
"""
