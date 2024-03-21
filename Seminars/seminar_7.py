"""Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
import random as rnd


def pairs_numbers(lines: int, file_name: str):
    MIN_NUM = -1000
    MAX_NUM = 1000

    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range(lines):
            f.write(
                f"{rnd.randint(MIN_NUM, MAX_NUM)}|{rnd.uniform(MIN_NUM, MAX_NUM)}\n"
            )
# pairs_numbers(5, 'numbers.txt')  # создаем файл numbers.txt с 5 парами чисел

"""Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл."""
# import random as rnd
import string


def write_name():
    name = ""
    while len(name) < rnd.randint(4, 6):
        name += rnd.choice(string.ascii_lowercase) * rnd.randint(0, 1) + rnd.choice(
            "aeioyu"
        ) * rnd.randint(0, 1)

    with open("names.txt", "a", encoding="utf-8") as f:
        f.write(name.title() + "\n")

# for _ in range (10):  # создаем файл и записываем в него 10 имен
#     write_name()

"""Задание №3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых 
задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    ✔ если результат умножения отрицательный, сохраните имя записанное строчными 
    буквами и произведение по модулю
    ✔ если результат умножения положительный, сохраните имя прописными буквами и 
    произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало."""

# читаем файлы и возвращаем кортеж списков значений из фалов
def _read_files(file1, file2) -> tuple[list[str], list[float]]:
    with (
        open(file1, "r", encoding="utf-8") as n,
        open(file2, "r", encoding="utf-8") as num,
    ):
        names = list(map(str.rstrip, n.readlines()))
        nums = [
            int(num.split("|")[0]) * float(num.split("|")[1])
            for num in map(str.rstrip, num.readlines())
        ]
    return names, nums

# выравниваем количество значений в списках
def _equality(list1: list[str], list2: list[float]) -> tuple[list[str], list[float]]:
    if len(list1) > len(list2):
        for i in range(len(list1) - len(list2)):
            list2.append(list2[i % len(list2)])
    elif len(list2) > len(list1):
        for i in range(len(list2) - len(list1)):
            list1.append(list1[i % len(list1)])
    return list1, list2


result = _read_files("names.txt", "numbers.txt")
result = _equality(result[0], result[1])

# записываем значения в новый файл в соответсвии с условием задачи
def write_name_number(data: tuple[list[str], list[float]]):
    with open("result.txt", "w", encoding="utf-8") as res:
        for name, number in zip(*data):
            if number < 0:
                res.write(f"{name.lower()} {abs(number)}\n")
            else:
                res.write(f"{name.upper()} {round(number)}\n")


write_name_number(result)
