"""Функция группового переименования файлов
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. 
Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется 
порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих 
файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы 
с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. 
Далее счётчик файлов и расширение. (!!! ЭТО УСЛОВНИЕ ТЕСТАМИ НЕ ПРОВЕРЯЕТСЯ!!!)
f. Папка test_folder доступна из текущей директории
"""

import os


def rename_files(
    desired_name="new_file_",
    num_digits=3,
    source_ext="doc",
    target_ext="txt",
):
    os.chdir("test_folder")
    num = 0
    for name in os.listdir():
        if name.endswith(source_ext):
            num += 1
            new_name = f"{desired_name}{str(num).zfill(num_digits)}.{target_ext}"
            os.rename(name, new_name)


"""Пакет для работы с файлами 1
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
Создайте файл __init__.py и запишите в него функцию rename_files
"""
import os

func_rename = """
import os

def rename_files(desired_name="new_file_",
                num_digits=3,
                source_ext="doc",
                target_ext="txt",
                ):
    os.chdir('test_folder')
    num = 0
    for name in os.listdir():
        if name.endswith(source_ext):
            num+=1
            new_name = f'{desired_name}{str(num).zfill(num_digits)}.{target_ext}'
            os.rename(name, new_name)
"""

name_list = [
    name.split(".")[0]
    for name in os.listdir()
    if os.path.isfile(name) and name != "__init__.py"
]

with open("__init__.py", "w", encoding="utf-8") as f:
    f.write(f"__all__ = {name_list}\n")
    f.write(func_rename)
