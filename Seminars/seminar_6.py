"""Задание №1
Вспомните какие модули вы уже проходили на курсе.
Создайте файл, в котором вы импортируете встроенные в
модуль функции под псевдонимами. (3-7 строк импорта).
"""

import random as rnd
from pandas import pivot as pv, infer_freq as i_f
from sys import base_exec_prefix

# так НЕЖЕЛАТЕЛЬНО делать:
from math import *

# лучшее так:
import math


"""Задание №2
� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
"""
from random import randint


# var 1
def guess_number(num1: int, num2: int, num3: int) -> bool:
    print(f"Угадай число от {num1} до {num2}, у тебя {num3} попыток")
    ans_number = randint(num1, num2)
    while num3:
        user_num = int(input("Введите число: "))
        if user_num == ans_number:
            return True
        elif user_num < ans_number:
            print("Больше")
        elif user_num > ans_number:
            print("Меньше")
        num3 -= 1
    return False


print(guess_number(1, 100, 3))


# var 2
def guess(max_height, min_height, count):
    b = randint(max_height, min_height)
    for _ in range(count):
        a = int(input("число: "))
        if a == b:
            return True
        elif a > b:
            print("больше")
        elif a < b:
            print("меньше")
    return False


"""Задание №3
� Улучшаем задачу 2.
� Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
� Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
"""
from sys import argv
from task3 import guess_number

"""был создан отдельный файл task3.py, в которм лежал код:
from random import randint

def guess_number(num1: int, num2: int, num3: int) -> bool:
    print(f"Угадай число от {num1} до {num2}, у тебя {num3} попыток")
    ans_number = randint(num1, num2)
    while num3:
        user_num = int(input("Введите число: "))
        if user_num == ans_number:
            return True
        elif user_num < ans_number:
            print("Больше")
        elif user_num > ans_number:
            print("Меньше")
        num3 -= 1
    return False


def riddles(quesion: str, answers: list[str], tryes: int) -> str:
    print(f"Отгадай загадку: \n{quesion}")
    true_answer = list(map(lambda x: x.lower(), answers))
    while tryes:
        for i in range(1, tryes + 1):
            print(f"Осталось попыток: {tryes}")
            user_answer = input("Введите отгадку: ").lower()
            if user_answer in true_answer:
                return i
            else:
                print("Не угадал! попробуй еще раз")
            tryes -= 1
    return 0
"""

# var 1
num_list = list(map(int, argv[1:4]))
print(guess_number(*num_list))


# var 2
num_list = list(map(int, argv[1:4]))

low_limit, high_limit, tries = 1, 100, 10

if len(num_list) == 1:
    high_limit = num_list[0]
elif len(num_list) == 2:
    low_limit, high_limit = num_list
else:
    low_limit, high_limit, tries = num_list

print(guess_number(low_limit, high_limit, tries))

"""Задание №4
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
� Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.
"""
riddl = "Зимой и летом одним цветом"
answer = ["Ель", "елка", "сосна"]


# var 1
def riddles(quesion: str, answers: list[str], tryes: int) -> str:
    print(f"Отгадай загадку: \n{quesion}")
    true_answer = list(map(lambda x: x.lower(), answers))
    while tryes:
        for i in range(1, tryes + 1):
            print(f"Осталось попыток: {tryes}")
            user_answer = input("Введите отгадку: ").lower()
            if user_answer in true_answer:
                return f"Отгадал с {i}-й попытки"
            else:
                print("Не угадал! попробуй еще раз")
            tryes -= 1
    return "Попытки закончились"


print(riddles(riddl, answer, 4))


# var 2 Шамиль
def guess_riddle(riddle, options, count):
    for attempt in range(1, count + 1):
        print(riddle)
        print(["ночное небо", "звезда", "морская волна"])
        guess = input(f"Попытка {attempt}. Введите свой вариант: ").strip().lower()
        print(["ночное небо", "звезда", "морская волна"])
        if guess in options:
            print("Поздравляем! Вы угадали загадку!")
            return attempt
        else:
            print("Неправильно. Попробуйте еще раз.")
    print("Попытки исчерпаны. Загадка не отгадана.")
    return 0


riddle = "Что это такое: синий, большой, с усами и полностью набит звездами?"
options = ["ночное небо", "звезда", "морская волна"]
count = 3
result = guess_riddle(riddle, options, count)
if result:
    print(f"Загадка отгадана с попытки номер {result}.")
else:
    print("Загадка не отгадана.")


# var 3 Stone
def questions(question: str, answers: list[str], tries: int) -> int:
    print(question)
    for user_tries in range(1, tries + 1):
        user_answer = input("Ваш вариант ответа: ")
        if user_answer.lower() in list(map(lambda x: x.lower(), answers)):
            return user_tries
        else:
            print(f"Ответ неверный! Осталось еще {tries - user_tries} попыток")
    return 0


"""Задание №5
� Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
� Ключ словаря - загадка, значение - список с отгадками.
� Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""
# var 1
from task3 import riddles


def play_riddles(riddle_data: dict[str, list[str], count:int]):
    for riddle, answer in riddle_data.items():
        ans_count = riddles(riddle, answer, count)
        result = []
        result.append(
            f"Загадка {riddle} "
            + (f"отгадана с {ans_count} попытки" if ans_count else "не отгадана")
        )

    return result


# var 2
from task_03 import questions
from random import choice


def play_puzzles(puzzles_data: dict[str, list[str]], count: int, tries: int) -> str:
    result = []
    while len(puzzles_data) and count:
        puzzle = choice(list(puzzles_data))
        answers = puzzles_data.pop(puzzle)
        puzzle_count = questions(puzzle, answers, tries)
        result.append(
            f'Загадка "{puzzle}"'
            + (
                f" отгадана с {puzzle_count} попытки"
                if puzzle_count
                else " не отгадана"
            )
        )
        count -= 1
    return "\n".join(result)


if __name__ == "__main__":
    puzzles = {
        "Ни лает, ни кусает, в дом не пускает?": ["замок", "сигнализация"],
        "Висит груша, нельзя скушать?": ["лампочка", "лампа"],
        "Зимой и летом одним цветом?": ["ель", "ёлка"],
    }
    print(play_puzzles(puzzles, 4, 3))

"""Задание №6
� Добавьте в модуль с загадками функцию, которая
принимает на вход строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение.
"""
from task_03 import questions
from random import choice

_dict_answers = {}


def play_puzzles(puzzles_data: dict[str, list[str]], count: int, tries: int) -> str:
    while len(puzzles_data) and count:
        puzzle = choice(list(puzzles_data))
        answers = puzzles_data.pop(puzzle)
        puzzle_count = questions(puzzle, answers, tries)
        _dict_answers[puzzle] = (
            f"Отгадана с {puzzle_count} попытки" if puzzle_count else " не отгадана"
        )
        count -= 1


def print_answers():
    for puzzle, answer in _dict_answers.items():
        print(f"\nЗагадка: {puzzle}\n{answer}")


if __name__ == "__main__":
    puzzles = {
        "Ни лает, ни кусает, в дом не пускает?": ["замок", "сигнализация"],
        "Висит груша, нельзя скушать?": ["лампочка", "лампа"],
        "Зимой и летом одним цветом?": ["ель", "ёлка"],
    }
    play_puzzles(puzzles, 4, 3)
    print_answers()


"""
Задание №7
� Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию.
"""


# var 1
def true_year(date: str) -> bool:
    day, month, year = map(int, date.split("."))
    result = []
    if 0 < year <= 9999:
        result.append(True)

    if month in (1, 3, 5, 7, 8, 10, 12) and 0 < day <= 31:
        result.append(True)

    if month in (4, 6, 9, 11) and 0 < day <= 30:
        result.append(True)

    if month == 2:
        if _leap_year(year):
            if 0 < day <= 29:
                result.append(True)
        else:
            if 0 < day <= 28:
                result.append(True)

    if len(result) == 2:
        return True
    return False


def _leap_year(year):
    return True if not year % 400 or not year % 4 and year % 100 else False


user_date = "51.01.2024"
print(true_year(user_date))


# var 2
def _is_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_data(data):
    day, month, year = map(int, data.split("."))
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 2:
        if _is_year(year):
            return day <= 29
        else:
            return day <= 28
    elif month in [4, 6, 9, 11]:
        return day <= 30
    else:
        return True


print(is_data("25.13.2025"))


# var 3 Stone
def _is_leap(current_year: int) -> bool:
    return not current_year % 4 and current_year % 100 or not current_year % 400


def date_validate(user_date: str) -> bool:
    day, month, year = map(int, user_date.split("."))
    _months = {i: 30 if i in (4, 6, 9, 11) else 31 for i in range(1, 13)}
    _months[2] = 29 if _is_leap(year) else 28

    if 0 < year < 10000 and month in _months and 0 < day <= _months[month]:
        return True
    return False


print(date_validate("29.02.2024"))
print(date_validate("29.02.2023"))
print(date_validate("29.13.2024"))
print(date_validate("29.02.20245"))
