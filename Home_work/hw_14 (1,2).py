'''
Класс Rectangle - работа с прямоугольниками doctest
'''
class NegativeValueError(Exception):
    def __init__(self, value, text) -> None:
        self.value = value
        self.text = text

    def __str__(self) -> str:
        return f"{self.text} должна быть положительной, а не {self.value}"


class Rectangle:
    def __init__(self, width, height=None):
        """
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r4 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -2
        """
        if isinstance(width, (int, float)) and width > 0:
            self.width = width
        else:
            raise NegativeValueError(width, "Ширина")
        if height is None:
            self.height = width
        else:
            if isinstance(height, (int, float)) and height > 0:
                self.height = height
            else:
                raise NegativeValueError(height, "Высота")

    def perimeter(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r1.area()
        25
        >>> r2.area()
        12
        """
        return self.width * self.height

    def __add__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
# # в тест ГБ ставлять не нужно:
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)


'''
Rectangle тесты unittest
'''

class TestRectangle(unittest.TestCase):
    def test_width(self):
        self.assertEqual(Rectangle(5).width, 5)

    def test_height(self):
        self.assertEqual(Rectangle(3, 4).height, 4)

    def test_perimeter(self):
        self.assertEqual(Rectangle(5).perimeter(), 20)

    def test_area(self):
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_addition(self):
        self.assertEqual(Rectangle(5) + Rectangle(3, 4), Rectangle(8, 6.0))
