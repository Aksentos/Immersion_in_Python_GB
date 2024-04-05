'''Генерация случайных данных и нахождение корней квадратного уравнения
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать 
по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл. 
Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения 
вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. 
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит 
параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json 
будет сохранена информация о параметрах и результатах вычислений для каждой строки данных 
из CSV-файла.
'''
import csv
import json
from random import randint


def generate_csv_file(file_name: str, rows: int):
    with open(file_name, "w", newline="", encoding="utf-8") as csf:
        csv_write = csv.writer(csf, dialect="excel", delimiter=" ")
        for _ in range(rows):
            nums_data = [randint(-1000, 1000) for _ in range(3)]
            csv_write.writerow(nums_data)


def save_to_json(func):
    def wrapper(*args):
        with open(args[0], "r", newline="", encoding="utf-8") as csv_read:
            csv_f = csv.reader(csv_read, dialect="excel")
            data = []
            for line in csv_f:
                a, b, c = map(int, line[0].split())
                result = func(a, b, c)
                data.append({"parameters": [a, b, c], "result": result})
        with open("results.json", "w", encoding="utf-8") as js_file:
            json.dump(data, js_file, indent=4)

    return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        return x1, x2
    elif not d:
        return -b / (2 * a)
    return None


# Пакет для работы с файлами 3
with open('__init__.py', 'w', encoding="utf-8") as init_file:
    data = ['def save_to_json', 'def find_roots', 'def generate_csv_file']
    for item in data:
        init_file.write(item + '\n')
