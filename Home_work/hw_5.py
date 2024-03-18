""" Информация о файле
✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

# Для тестов:
# file_path = "C:/Users/User/Documents/example.txt"
## должен быть ответ: ('C:/Users/User/Documents/', 'example', '.txt')
# file_path = "file_in_current_directory.txt"
## должен быть ответ: ('', 'file_in_current_directory', '.txt')
# file_path = '/home/user/docs/my.file.with.dots.txt'
## должен быть ответ: ('/home/user/docs/', 'my.file.with.dots', '.txt')


# var 1 (однострочник)
def get_file_info(file_path: str) -> tuple:
    return (
        file_path.rpartition("/")[0] + "/" * bool(file_path.rpartition("/")[0]),
        file_path.rpartition("/")[2].rpartition(".")[0],
        "." + file_path.rpartition("/")[2].rpartition(".")[-1],
    )


# var 2 GB
def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[: -len(file_name)]
    return (path, file_name[: -len(file_extension) - 1], "." + file_extension)


"""Однострочный генератор словаря
Напишите однострочный генератор словаря, который принимает на вход три списка 
одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в 
качестве значения.

Сумма рассчитывается как ставка умноженная на процент премии.

Не забудьте распечатать в конце результат.
"""

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]


# var 1
def gen_dict(names, salary, bonus) -> dict:
    return {
        name: sal * int(bon[:-1]) / 100 for name, sal, bon in zip(names, salary, bonus)
    }


print(gen_dict(names, salary, bonus))


# var 2 GB
result = {
    names[i]: round(salary[i] * float(bonus[i].strip("%")) / 100, 2)
    for i in range(len(names))
}
print(result)


"""Генератор чисел Фибоначчи
Создайте функцию генератор чисел Фибоначчи fibonacci.
"""


# var 1
def fibonacci():
    value1 = 0
    value2 = 1
    counter = 0
    temp = 0
    while True:
        if counter < 3:
            yield value1
            counter += 1
            value1 = value2
        else:
            temp = value1 + value2
            yield temp
            value1 = value2
            value2 = temp


# var 2 GB (крутяк в кои-то веки)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
