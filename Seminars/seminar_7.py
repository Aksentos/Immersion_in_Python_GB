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

"""Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
    ✔ расширение
    ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
    ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
    ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
    ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
    ✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона."""

import string
import random


def add_file(
    expansion,
    MIN_NAME_LENGHT=6,
    MAX_NAME_LENGHT=30,
    MIN_BITES=256,
    MAX_BITES=4096,
    FILES_QUANTITY=42,
):

    for _ in range(FILES_QUANTITY):
        name = "".join(
            random.choices(
                string.ascii_lowercase + string.digits,
                k=random.randint(MIN_NAME_LENGHT, MAX_NAME_LENGHT),
            )
        )

        data = bytes(
            random.randint(0, 255) for _ in range(random.randint(MIN_BITES, MAX_BITES))
        )
        if f'{name}.{expansion}' not in os.listdir():
            with open(f"{name}.{expansion}", "wb") as f:
                f.write(data)


add_file("txt", FILES_QUANTITY=5)

"""Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""

expansions = ["txt", "jpeg", "bin", "avi", "mp3"]


def add_files(*args, quantity=1):
    if quantity == 1:
        for exp in args:
            add_file(exp, FILES_QUANTITY=1)
    else:
        for exp in args:
            add_file(exp, FILES_QUANTITY=random.randint(1, quantity))


"""Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён."""

import os


def add_file_to_dir(dir):
    if dir not in os.listdir():
        os.mkdir(dir)
    os.chdir(dir)
    add_files(*expansions, quantity=2)


add_file_to_dir('new_dir')


"""Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""

from pathlib import Path


def folders():
    try:
        Path("video").mkdir()
        Path("foto").mkdir()
        Path("bins").mkdir()
        Path("text").mkdir()
    except:
        print("Папки уже существуют")


def send_files_to_dir():
    for obj in Path(Path().cwd()).iterdir():
        if obj.is_file():
            file = str(obj).rsplit("\\", maxsplit=1)[-1]
            if file.endswith(("txt", "doc", "docx")):
                Path(file).replace(Path.cwd() / "text" / file)
            elif file.endswith(("avi", "mp4", "mkv")):
                Path(file).replace(Path.cwd() / "video" / file)
            elif file.endswith("jpeg"):
                Path(file).replace(Path.cwd() / "foto" / file)
            elif file.endswith("bin"):
                Path(file).replace(Path.cwd() / "bins" / file)


folders()
add_files(*expansions, quantity=3)
send_files_to_dir()
