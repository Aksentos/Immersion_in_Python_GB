"""
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток. """

import random
from typing import Callable


def random_number_game(min_number: int, max_number: int, count: int) -> Callable:
    random_number = random.randint(min_number, max_number)
    print(f"Отгадайте число от {min_number} до {max_number}. Попыток {count}")

    def check_random():
        for _ in range(count):
            user = int(input("Введите число: "))
            if user == random_number:
                print("Поздравляем!")
                return
            elif user < random_number:
                print("Загаданное число больше")
            else:
                print("Загаданное число меньше")
        print(f"К сожалению вы исчерпали {count} попыток. Число было {random_number}")

    return check_random


# MIN_NUMBER = 1
# MAX_NUMBER = 100
# COUNT = 5
# result = random_number_game(MIN_NUMBER, MAX_NUMBER, COUNT)
# result()


"""Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""


def validator(func):
    def wrapper(num: int, attempts: int) -> None:
        if not 0 < num < 101:
            num = random.randint(1, 100)
        if not 0 < attempts < 11:
            attempts = random.randint(1, 10)
        return func(num, attempts)

    return wrapper


# @validator
# def guess_num(num: int, attempts: int) -> None:
#     for attempt in range(attempts):
#         try:
#             guess = int(
#                 input(
#                     f"Введите целое число от 1 до 100 "
#                     f"(попытка {attempt + 1} из {attempts}): \n"
#                 )
#             )
#             if guess == num:
#                 print(f"Вы угадали! Загаданное число - {num}")
#                 break
#             else:
#                 print(f"Вы не угадали!")
#         except ValueError:
#             print("Ошибка ввода, необходимо ввести целое число")

#     else:
#         print(f"Вы проиграли! Загаданное число - {num}")


# if __name__ == "__main__":
#     guess_num(120, 5)


"""Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""

import os
import json


def json_writer(func):
    def wrapper(*args, **kwargs):
        file_name = f"{func.__name__}.json"
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="UTF-8") as file:
                data_json = json.load(file)
                current_id = int(max(data_json)) + 1
        else:
            data_json = {}
            current_id = 1
        result = func(args, kwargs)
        data_json[current_id] = {
            "func_name": func.__name__,
            "result": result,
            "args": args,
            "kwargs": {},
        }
        for key, value in kwargs.items():
            data_json[current_id]["kwargs"][key] = value
        with open(file_name, "w", encoding="UTF-8") as file:
            json.dump(data_json, file, indent=4, ensure_ascii=False)

    return wrapper


# @json_writer
# def summa_args(*args, **kwargs):
#     return sum(args[0])


"""Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""

import random
from typing import Callable


# var 1
def count(num: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            counter = []
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter

        return wrapper

    return deco


@count(5)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f"{rnd(1, 10) = }")


# var 2
def repeat(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper

    return decorator


# @repeat(5)
# def example_func(x, y):
#     return x + y


# print(example_func(1, 5))

"""Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""

'''Задание №6
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
'''
@repeat(2)
@json_writer
@validator
def guess_number_game(min_number: int, max_number: int, count: int) -> int:
    secret_number = random.randint(min_number, max_number)
    print(f"Отгадайте число от {min_number} до {max_number}. У вас {count} попыток.")
    for _ in range(count):
        guess = int(input("Введите ваше предположение: "))
        if guess == secret_number:
            print("Поздравляем! Вы угадали число!")
            return 1
        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
    print(f"К сожалению, вы исчерпали все {count} попыток. Загаданное число было {secret_number}.")
    return 0

# Пример использования:
guess_number_game(1, 100, 2)


'''ОТ КИРИЛЛА'''
import os
import json


def counter(number):
    def outter(func):
        result = []

        def inner(*args, **kwargs):
            for _ in range(number):
                result.append(func(*args, **kwargs))
            return result

        return inner

    return outter


def json_writer(func):
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data_json = json.load(file)
                current_id = int(max(data_json, key=lambda x: int(x))) + 1
        else:
            data_json = {}
            current_id = 1
        result = func(*args, **kwargs)
        data_json[current_id] = {'func_name': func.__name__, 'result': result, 'args': args, 'kwargs': {}}
        for key, value in kwargs.items():
            data_json[current_id]['kwargs'][key] = value
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data_json, file, indent=4, ensure_ascii=False)

    return wrapper


@counter(5)
@json_writer
def summa_args(*args, **kwargs):
    return sum(map(int, args))


summa_args(1, 2, 8, 8, 9, 78, 90, k='6', l='8', h=78)
