"""Задача по обходу и анализу файловой системы
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно 
обходит эту директорию и все вложенные директории. Результаты обхода должны быть 
сохранены в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать 
следующую информацию:

Путь к файлу или директории: Абсолютный путь к файлу или директории. 
Тип объекта: Это файл или директория. 
Размер: Для файлов - размер в байтах, для директорий - размер, 
учитывая все вложенные файлы и директории в байтах. 

Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри 
данной директории, и вложенных директорий.
Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть 
выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.
Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход 
директории и возвращать результаты в виде списка словарей. После этого результаты должны быть 
сохранены в трех различных файлах (JSON, CSV и Pickle) с помощью функций 
save_results_to_json, save_results_to_csv и save_results_to_pickle.

Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном 
обходе директорий. При этом сначала добавляются файлы, а затем директории.

Для каждого файла (name в files), сначала создается полный путь к файлу 
(path = os.path.join(root, name)), и затем получается размер файла (size = os.path.getsize(path)). 
Информация о файле добавляется в список results в виде словаря 
{'Path': path, 'Type': 'File', 'Size': size}.

Затем, для каждой директории (name в dirs), также создается полный путь к директории 
(path = os.path.join(root, name)), и вызывается функция get_dir_size(path), чтобы получить размер 
всей директории с учетом ее содержимого. Информация о директории добавляется в список results в 
виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
"""


import os
import csv
import json
import pickle

# var 1 (автотест не принимает, но все работает)

def traverse_directory(directory: str):
    result = []
    for dir_path, _, file_name in os.walk(directory):
        size_dir = get_folder_size(dir_path)  # Размер папки в байтах
        abs_dir_path = os.path.abspath(dir_path)  # Абсолютный путь до папки
        # print(f'Родительская директория {Path(dir_path).parent.absolute()}\n')

        for file in file_name:
            abs_file_path = os.path.abspath(
                os.path.join(dir_path, file)
            )  # Абсолютный путь до файла
            size_file = os.path.getsize(abs_file_path)  # Размер файла в байтах
            result.append({"Path": abs_file_path, "Type": "File", "Size": size_file})

        result.append({"Path": abs_dir_path, "Type": "Directory", "Size": size_dir})
    return result


# Функция расчета размера директории в байтах
def get_folder_size(folder: str) -> int:
    folder_size = 0
    for dir_path, _, file_names in os.walk(folder):
        for file in file_names:
            folder_size += os.path.getsize(os.path.join(dir_path, file))
    return folder_size


def save_results_to_json(res_list: list[dict], name: str):
    with open(name, "w", encoding="utf-8") as js:
        json.dump(res_list, js, ensure_ascii=False, indent=4)


def save_results_to_csv(res_list: list[dict], name: str):
    with open(name, "w", encoding="utf-8") as cs:
        csv_write = csv.DictWriter(
            cs,
            fieldnames=["Path", "Type", "Size"],
            dialect="excel-tab",
            quoting=csv.QUOTE_NONNUMERIC,
        )
        csv_write.writeheader()

        for result in res_list:
            csv_write.writerow(result)


def save_results_to_pickle(res_list: list[dict], name: str):
    with open(name, "wb") as pcl:
        pickle.dump(res_list, pcl)



# var 2 GB
def get_dir_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)

    return total_size

def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})

        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})

    return results

def save_results_to_json(results, file_path):
    with open(file_path, 'w') as file:
        json.dump(results, file)

def save_results_to_csv(results, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(results, file)

'''Пакет для работы с файлами 2
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
'''

name_list = [
    "def get_dir_size",
    "def save_results_to_json",
    "def save_results_to_csv",
    "def save_results_to_pickle",
    "def traverse_directory",
]

with open("__init__.py", "w", encoding="utf-8") as f:
    for name in name_list:
        f.write(f"{name}\n")
