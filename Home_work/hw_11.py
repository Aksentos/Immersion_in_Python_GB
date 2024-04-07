"""Информация об авторе и времени создания
Разработайте программное обеспечение для ведения журнала событий. Вам необходимо
создать класс, который будет представлять строки журнала и включать в себя информацию
об авторе и времени создания каждой записи.

Условие задачи:
Создайте класс MyStr, который наследуется от встроенного класса str и добавляет
дополнительную информацию о создателе строки и времени ее создания. Этот класс
будет представлять строки с информацией о событиях.

Класс MyStr должен иметь следующие атрибуты и методы:
value (str): Строковое значение с описанием события.
author (str): Имя автора, создавшего запись.
time: Время создания записи в формате '%Y-%m-%d %H:%M'.

Магические методы (Dunder-методы):
Реализуйте метод __new__(cls, value, author), который создает новый объект класса
MyStr с заданным value и author. Метод также автоматически фиксирует время создания
записи. В этом методе создается новый объект MyStr с указанными атрибутами и текущим
временем в атрибуте time.

Реализуйте метод __str__(self), который возвращает строковое представление объекта
класса MyStr с информацией о событии, авторе и времени создания.

Реализуйте метод __repr__(self), который возвращает строковое представление объекта
класса MyStr.
Метод __repr__ возвращает строку, которая может быть использована для создания точно
такого же объектаMyStrс теми же значениямиvalueиauthor`.
"""

import time


class MyStr(str):
    """MyStr Класс создания строки с информацией об авторе и времени создания

    Args:
        str (_type_): наследумеся от класса str

    Dunder методы:
        __new__(cls, value, author): создает новый объект класса.
        _str__(): возвращает строковое представление объекта класса.
        __repr__(): возвращает строковое представление объекта класса для отладки.
    """

    def __new__(cls, value: str, author: str):
        """__new__ _summary_

        Args:
            value (str): строковое значение
            author (str): автор строки

        Returns:
            _type_: объект класса MyStr
        """
        instance = super().__new__(cls)
        instance.value = value
        instance.author = author
        instance.time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        return instance

    def __str__(self):
        return f"{self.value} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self) -> str:
        return f"MyStr('{self.value}', '{self.author}')"


# # проверка
# my_string = MyStr("Пример текста", author="Иван")
# print(my_string)
# my_string2 = MyStr("Мама мыла раму", "Маршак")
# # print(repr(my_string2))

"""Класс Archive - архив текстовых и числовых записей
Разработайте программу для хранения и управления текстовыми и числовыми записями.
Вам нужно создать класс Archive, который будет представлять архив и реализовывать 
следующую функциональность:

Методы и операции:
При создании экземпляра класса Archive с указанием текстовой и числовой записи (text и number), 
записи добавляются в соответствующие атрибуты archive_text и archive_number. Если архив уже 
существует, текущие записи (text и number) добавляются в архив.

Метод __str__ возвращает строковое представление объекта, включая текущие записи (text и number) 
и архивированные записи (archive_text и archive_number).

Метод __repr__возвращает строковое представление объекта, которое можно использовать для создания 
нового объекта того же класса с теми же записями.

Архивированные записи могут быть получены через атрибуты archive_text и archive_number.

Метод __new__ - это статический метод, который создает новый экземпляр класса. Первым аргументом 
метод __new__ получает ссылку на класс (cls), а затем может принимать дополнительные аргументы. 
Метод __new__ проверяет, существует ли уже экземпляр класса Archive (с использованием атрибута 
_instance). Если экземпляр существует, то метод вместо создания нового экземпляра добавляет 
текущие значения text и number в архив (списки archive_text и archive_number) для уже существующего 
экземпляра. Если экземпляр еще не существует, метод создает новый экземпляр класса Archive с пустыми 
архивами для текстовых и числовых записей. В любом случае метод возвращает созданный или 
существующий экземпляр класса Archive.

Метод __init__ - это конструктор экземпляра класса, который вызывается после создания экземпляра с 
использованием метода __new__. Метод __init__ принимает два аргумента: text (строка) и number 
(целое число или число с плавающей точкой). В методе __init__устанавливаются атрибуты text и number 
текущего экземпляра класса для хранения переданных текстовой и числовой записей. Эти записи могут 
быть затем добавлены в архив (списки archive_text и archive_number) с использованием метода __new__.
"""


class Archive:
    archive_text = []
    archive_number = []

    def __new__(cls, *args):
        _instance = super().__new__(cls)
        if isinstance(_instance, Archive):
            _instance.archive_text = cls.archive_text.copy()
            _instance.archive_number = cls.archive_number.copy()
            cls.archive_text.append(args[0])
            cls.archive_number.append(args[1])
        return _instance

    def __init__(self, text: str, number: float) -> None:
        self.text = text
        self.number = number
        self.archive_text.append(text)
        self.archive_number.append(number)

    def __str__(self) -> str:
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self) -> str:
        return f"Archive('{self.text}', {self.number})"


archive1 = Archive("Запись 1", 42)
archive2 = Archive("Запись 2", 3.14)
archive3 = Archive("Запись 3", 15)

print(archive1)
print(archive2)
print(archive3)
print(repr(archive3))


"""Задача 3
Класс Rectangle - работа с прямоугольниками"""


class Rectangle:
    """Класс создает объект - прямоугольники"""

    def __init__(self, width, height=None) -> None:
        self.width = width
        self.height = height if height else width

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


'''Задача о матричных операциях
Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.

Атрибуты класса:
rows (int): Количество строк в матрице.
cols (int): Количество столбцов в матрице.
data (list): Двумерный список, содержащий элементы матрицы.

__init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а 
также создает двумерный список data размером rows x cols и заполняет его нулями.

__str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка 
представляет матрицу, где элементы разделены пробелами, а строки разделены символами новой строки. 

__repr__(self): Метод, возвращающий строковое представление объекта, которое может быть 
использовано для создания нового объекта того же класса с такими же размерами и данными.

__eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает 
две матрицы и возвращает True, если они имеют одинаковое количество строк и столбцов, 
а также все элементы равны. Иначе возвращает False.

__add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, 
что обе матрицы имеют одинаковые размеры (количество строк и столбцов). Если размеры 
совпадают, создает новую матрицу, где каждый элемент равен сумме соответствующих 
элементов входных матриц.

__mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, 
что количество столбцов в первой матрице равно количеству строк во второй матрице. 
Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] 
равен сумме произведений элементов соответствующей строки из первой матрицы и столбца 
из второй матрицы.
'''

class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return "\n".join([" ".join(map(str, i)) for i in self.data])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.rows}, {self.cols})"

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.data[i][j] = self.data[i][j] + other.data[i][j]
            return new_matrix
        raise ValueError('Размерность матриц разная')

    def __mul__(self, other):
        if self.cols == other.rows:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    for k in range(self.cols):
                        new_matrix.data[i][j] += self.data[i][k] * other.data[k][j]
            return new_matrix
        raise ValueError('Размерность матриц разная')
