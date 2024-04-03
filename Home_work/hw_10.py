"""Создание класса-фабрики для животных
Создайте базовый класс Animal, который имеет атрибут name, 
представляющий имя животного.

Создайте классы Bird, Fish и Mammal, которые наследуются от 
базового класса Animal и добавляют дополнительные атрибуты и методы:

Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, 
который возвращает длину крыла птицы.

Fish имеет атрибут max_depth (максимальная глубина обитания) и 
метод depth, который возвращает категорию глубины рыбы (мелководная, 
средневодная, глубоководная) в зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она 
относится к категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к 
категории "Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".

Mammal имеет атрибут weight (вес) и метод category, который возвращает 
категорию млекопитающего (Малявка, Обычный, Гигант) в зависимости от 
веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".

Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры 
животных разных типов на основе переданного типа и параметров. 
Класс-фабрика должен иметь метод create_animal, который принимает 
следующие аргументы:

animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
*args - переменное количество аргументов, представляющих параметры для 
конкретного типа животного. Количество и типы аргументов могут 
различаться в зависимости от типа животного.

Метод create_animal должен создавать и возвращать экземпляр животного 
заданного типа с переданными параметрами.
Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция 
вызовет ValueError с сообщением 'Недопустимый тип животного'.
"""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Bird(Animal):
    def __init__(self, name: str, wingspan: float) -> None:
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self) -> float:
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name: str, max_depth: float) -> None:
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self) -> str:
        if self.max_depth < 10:
            return "Мелководная рыба"
        if self.max_depth > 100:
            return "Глубоководная рыба"
        return "Средневодная рыба"


class Mammal(Animal):
    def __init__(self, name: str, weight: float) -> None:
        super().__init__(name)
        self.weight = weight

    def category(self) -> str:
        if self.weight < 1:
            return "Малявка"
        if self.weight > 200:
            return "Гигант"
        return "Обычный"


class AnimalFactory(Bird, Fish, Mammal):

    def create_animal(animal_type: str, *args):
        if animal_type == "Bird":
            return Bird(args[0], args[1])
        if animal_type == "Fish":
            return Fish(args[0], args[1])
        if animal_type == "Mammal":
            return Mammal(args[0], args[1])
        raise ValueError("Недопустимый тип животного")


# Создание экземпляров животных
animal1 = AnimalFactory.create_animal("Bird", "Орел", 200)
animal2 = AnimalFactory.create_animal("Fish", "Лосось", 50)
animal3 = AnimalFactory.create_animal("Mammal", "Слон", 5000)


# Вывод результатов
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())

animal4 = AnimalFactory.create_animal("Spider", "Elephant", 5000)  # ValueError
print(animal4.category())


"""Лотерея Класс
На вход программе подаются два списка, каждый из которых содержит 
10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в 
этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, 
который будет сравнивать числа из вашего билета из list1 со списком 
выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.
"""


class LotteryGame:
    def __init__(self, tiket: list, lottery: list) -> None:
        self.tiket = tiket
        self.lottery = lottery

    def compare_lists(self):
        result = [i for i in self.tiket if i in self.lottery]
        if result:
            print(
                f"Совпадающие числа: {result}",
                f"Количество совпадающих чисел: {len(result)}",
                sep="\n",
            )
        else:
            print("Совпадающих чисел нет.")


list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
