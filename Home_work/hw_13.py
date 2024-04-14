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

'''Обработка исключений в Archive
Допишите в вашу задачу Archive обработку исключений.
Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, 
когда текст не является строкой или является пустой строкой.
Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'
И InvalidNumberError, которое будет вызываться, если число не является 
положительным целым числом или числом с плавающей запятой.
Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive 
integer or float.'
'''
from typing import Union

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if text and isinstance(text, str):
            self.text = text
        else:
            raise InvalidTextError(text)
        
        if isinstance(number, (int, float)) and number > 0:
            self.number = number
        else:
            raise InvalidNumberError(number)

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


class InvalidTextError(Exception):
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"Invalid text: {self.value}. Text should be a non-empty string."


class InvalidNumberError(Exception):
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"Invalid number: {self.value}. Number should be a positive integer or float."


# test 1
archive_instance = Archive("Sample text", 42.5)
print(archive_instance)
'''Ожидаемый ответ:
Text is Sample text and number is 42.5. Also [] and []
'''

# test 2
invalid_archive_instance = Archive("", -5)
print(invalid_archive_instance)
'''Ожидаемый ответ:
InvalidTextError: Invalid text: . Text should be a non-empty string.
'''

# test 3
invalid_archive_instance = Archive("Sample text", -5)
print(invalid_archive_instance)
'''Ожидаемый ответ:
__main__.InvalidNumberError: Invalid number: -5. Number should be a positive integer or float.

'''


