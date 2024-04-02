"""Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""


class Circle:
    PI = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    def lenght(self) -> float:
        return 2 * Circle.PI * self.radius

    def area(self) -> float:
        return Circle.PI * self.radius**2


c = Circle(3)
print(c.lenght(), c.area(), sep="\n")


"""Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


# var 1
class Rectangle:
    def __init__(self, lenght, width=0) -> None:
        self.lenght = lenght
        self.width = width if width else lenght

    def perimeter(self):
        return 2 * (self.width + self.lenght)

    def area(self):
        return self.width * self.lenght


rec = Rectangle(4, 10)
rec_sq = Rectangle(5)

print(rec.area(), rec.perimeter(), sep="\n")
print(rec_sq.area(), rec_sq.perimeter(), sep="\n")


# var 2
class Rectangle:
    def __init__(self, *args):
        self.args = args

    def perimeter(self):
        length = self.args[0]
        width = length if len(self.args) < 2 else self.args[1]
        return (length + width) * 2

    def square(self):
        length = self.args[0]
        width = length if len(self.args) < 2 else self.args[1]
        return length * width


"""Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Human:
    def __init__(
        self, last_name: str, name: str, patronymic: str, age: int, gender: str
    ) -> None:
        self.last_name = last_name
        self.name = name
        self.patronymic = patronymic
        self._age = age
        self.gender = gender

    def birthday(self) -> None:
        self._age += 1

    def full_name(self) -> str:
        return f"{self.last_name} {self.name} {self.patronymic}"

    def ages(self) -> str:
        return f"Возраст: {self._age}"


man1 = Human("Иванов", "Иван", "Иванович", 25, "муж")

print(man1.full_name(), man1.ages(), sep="\n")
man1.birthday()
print(man1.ages())


"""Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""


# var 1
class Employee(Human):
    def __init__(
        self, last_name: str, name: str, patronymic: str, age: int, gender: str, id: int
    ) -> None:
        super().__init__(last_name, name, patronymic, age, gender)
        self.id = id if len(str(id)) == 6 else 111111

        # self.level = self.access_level()

    @property
    def access_level(self) -> int:
        acc_lvl = sum(map(int, str(self.id)))
        return acc_lvl % 7


man1 = Employee("Иванов", "Иван", "Иванович", 25, "муж", 789456)

print(man1.access_level)
man1.id = 777777
print(man1.access_level)


# var 2
class Employee(Human):
    def __init__(
        self, last_name: str, name: str, patronymic: str, age: int, gender: str, id: int
    ) -> None:
        super().__init__(last_name, name, patronymic, age, gender)
        self.id = id if len(str(id)) == 6 else 111111
        self.level = self.access_level()

    def access_level(self) -> int:
        acc_lvl = sum(map(int, str(self.id)))
        return acc_lvl % 7


man1 = Employee("Иванов", "Иван", "Иванович", 25, "муж", 789456)

print(man1.level)
man1.id = 777777
print(man1.level)


"""Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Bird:
    def __init__(self, name, age, speed) -> None:
        self.name = name
        self.age = age
        self.speed = speed

    def speciific_property(self):
        return self.speed

    def __str__(self) -> str:
        return f"Имя птички: {self.name}, возраст: {self.age}"


class Dog:
    def __init__(self, name, age, voice) -> None:
        self.name = name
        self.age = age
        self.voice = voice

    def speciific_property(self):
        return self.voice

    def __str__(self) -> str:
        return f"Имя собаки: {self.name}, возраст: {self.age}"


class Fish:
    def __init__(self, name, age, depth) -> None:
        self.name = name
        self.age = age
        self.depth = depth

    def speciific_property(self):
        return self.depth

    def __str__(self) -> str:
        return f"Имя рыбки: {self.name}, возраст: {self.age}"


dog1 = Dog("Чарли", 12, "Гав")
bird1 = Bird("Чики", 3, 15)
fish1 = Fish("Клоун", 1, 5)

print(dog1.speciific_property())
print(dog1.voice)
print(bird1)


"""Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name, age, spec) -> None:
        self.name = name
        self.age = age
        self.spec = spec

    def __str__(self) -> str:
        return f"Имя: {self.name}, возраст: {self.age}"

    def speciific_property(self):
        return self.spec


class Bird(Animal):
    def __init__(self, name, age, speed) -> None:
        super().__init__(name, age, speed)
        self.speed = speed


class Dog(Animal):
    def __init__(self, name, age, voice) -> None:
        super().__init__(name, age, voice)
        self.voice = voice


class Fish(Animal):
    def __init__(self, name, age, depth) -> None:
        super().__init__(name, age, depth)
        self.depth = depth


dog1 = Dog("Чарли", 12, "Гав")
bird1 = Bird("Чики", 3, 15)
fish1 = Fish("Клоун", 1, 5)


print(dog1.speciific_property())
print(dog1.voice)
print(bird1)
