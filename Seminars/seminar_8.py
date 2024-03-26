"""Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json

def create_json(in_file, out_file):
    with open(in_file, "r", encoding="UTF-8") as input_file:
        data = input_file.readlines()
    data = {
        row.strip().split()[0].capitalize(): float(row.strip().split()[1])
        for row in data
    }
    with open(out_file, "w", encoding="UTF-8") as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)


create_json("names.txt", "names.json")


"""Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""

import json
import os


def input_name(message: str) -> str:
    return input(message)


def input_lvl(message: str, error_message: str, limits: tuple[int, int]) -> str:
    while True:
        level = input(message)
        if level.isdigit() and limits[0] <= int(level) <= limits[1]:
            return level
        print(error_message)


def input_id(
    message: str, error_message: str, id_is_exists: str, id_list: list[str]
) -> str:
    while True:
        user_id = input(message)
        if user_id.isdigit():
            if user_id not in id_list:
                return user_id
            else:
                print(id_is_exists)
        else:
            print(error_message)


def input_users(file_name: str) -> None:
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            users_dict = json.load(file)
    else:
        users_dict = {}
    users_id_list = [u_id for users in users_dict.values() for u_id in users]
    while True:
        user_name = input_name("Введите имя пользователя: ")
        if not user_name:
            break
        user_id = input_id(
            "Введите ID пользователя: ",
            "ID должен состоять исключительно из цифр!",
            "Пользователь с таким ID уже существует!",
            users_id_list,
        )
        user_level = input_lvl(
            "Введите уровень доступа пользователя от 1 до 7: ",
            "Нужно ввести число от 1 до 7!",
            (1, 7),
        )
        # users_levels_list = sorted(users_dict, key=lambda x: int(x))
        # users_dict = {user_lvl: users_dict[user_lvl] for user_lvl in users_levels_list}
        if user_level in users_dict:
            users_dict[user_level][user_id] = user_name
        else:
            users_dict[user_level] = {user_id: user_name}
        with open(file_name, "w", encoding="UTF-8") as file:
            json.dump(users_dict, file, indent=4, ensure_ascii=False, sort_keys=True)
        users_id_list.append(user_id)


input_users("user_list.json")


"""Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""

import json
import csv


def convert_to_csv(json_file, csv_file):
    with (
        open(json_file, "r", encoding="UTF-8") as users_json,
        open(csv_file, "w", encoding="UTF-8", newline="") as users_csv,
    ):
        data = json.load(users_json)
        csv_writer = csv.writer(users_csv)
        csv_writer.writerow(["name", "ID", "level"])

        for user_lvl, users in data.items():
            for user_id, user_name in users.items():
                csv_writer.writerow([user_name, user_id, user_lvl])


convert_to_csv("user_list.json", "task_3_2.csv")


"""Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import json
import csv


def new_user_json(input_file_name: str, output_file_name: str):
    with (
        open(input_file_name, "r", encoding="UTF-8") as in_csv_data,
        open(output_file_name, "w", encoding="UTF-8") as out_json_file,
    ):
        data = {}
        csv_reader = csv.reader(in_csv_data)
        for i, row in enumerate(csv_reader):
            if i:
                user_data = [row[0].lower(), row[1].zfill(10), row[2]]
                data[hash(user_data[0] + user_data[1])] = user_data
        json.dump(data, out_json_file, indent=4, ensure_ascii=False, sort_keys=True)


new_user_json("task_3_2.csv", "new_user.json")

"""Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""

import os
import json
import pickle


def serialize_json(directory):
    if not os.path.exists(directory):
        print("Директория не найдена")
        return

    files = [file for file in os.listdir(directory) if file.endswith(".json")]

    for file_name in files:
        json_path = os.path.join(directory, file_name)
        pickle_path = os.path.join(directory, file_name.split(".")[0] + ".pickle")

        with (
            open(json_path, "r", encoding="UTF-8") as json_file,
            open(pickle_path, "wb") as pickle_file,
        ):
            data = json.load(json_file)
            pickle.dump(data, pickle_file)


serialize_json(".")


"""Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import os
import csv
import pickle


def pickle_to_csv(path_pickle: str, headers: list[str]):
    current_path_pickle = os.path.split(path_pickle)
    path_csv = os.path.join(
        current_path_pickle[0], current_path_pickle[-1].split(".")[0] + ".csv"
    )
    with (
        open(path_pickle, "rb") as pickle_file,
        open(path_csv, "w", encoding="UTF-8") as csv_file,
    ):
        data = pickle.load(pickle_file)
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)
        for user_level, user in data.items():
            for user_id, user_name in user.items():
                csv_writer.writerow([user_name, user_id, user_level])


pickle_to_csv("user_list.pickle", ["name", "id", "level"])


"""Задание №7
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import pickle


def print_pickle(path_csv: str):
    with open(path_csv, "r", encoding="UTF-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = [row for row in csv_reader]
        print(pickle.dumps(data))


print_pickle("user_csv.csv")
