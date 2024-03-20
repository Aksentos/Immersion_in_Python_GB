"""Проверка корректности даты
Вы работаете над разработкой программы для проверки корректности даты,
введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
в зависимости от результата проверки."""

# var 1
date_to_prove = "29.2.2024"


def is_date(date: str) -> bool:
    day, month, year = map(int, date.split("."))
    date_dict = {m: 30 if m in (4, 6, 9, 11) else 31 for m in range(1, 13)}
    date_dict[2] = 29 if not year % 400 or not year % 4 and year % 100 else 28
    return (
        True
        if 0 < month < 13 and 0 < day <= date_dict[month] and 0 < year < 10000
        else False
    )


print(is_date(date_to_prove))


# var 2 GB
from sys import argv


def is_leap(year: int):
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


def valid(full_date: str):
    date, month, year = (int(item) for item in full_date.split("."))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True


if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove))

""" Задача о 8 ферзях
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Не забудьте напечатать результат.
"""


# var 1
Проверяем, бьют ли ферзи друг друга
def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1]:  # вертикаль и горизонталь
        return True
    elif abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):  # диагонали
        return True
    return False


# Проверяем все возможные пары ферзей
def check_queens(queens):
    for i in range(len(queens)):
        for j in range(len(queens) - 1, i, -1):
            if is_attacking(queens[i], queens[j]):
                # print(f'ферзь {queens[i]} и ферзь {queens[j]} бьют друг друга')
                return False
    return True

q = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
print(check_queens(queens = q))


# var 2 GB
from itertools import combinations


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


"""Расстановка ферзей
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка 
ферзей на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами, 
ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали 
или диагонали.

Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его 
не надо."""
from random import randint as rni

def generate_boards():
    board_list = []
    while len(board_list) < 4:
        q_list = []  # список для положений ферзей
        counter = 0  # счетчик для остановки цикла
        while len(q_list) < 8:
            queen = (rni(1,8), rni(1,8))  # формируем позицию ферзя
            q_list.append(queen)  # добавляем ферзя в список
            if not check_queens(q_list):  # проверяем пары функцией из предыдущей задачи 
                q_list.pop() # если пара неподходит, удаляем её
            counter += 1
            if counter == 64:  # если счетчик достиг 64, вариант не найден, начинаем заново
                break
        if len(q_list) == 8:  # если в списке 8 ферзей добавляем наш список в итоговый список
            board_list.append(q_list)
    return board_list

print(generate_boards())

# код от GB вставлять не стал, тк:
# Время работы моего кода: 0.06820869445800781 с; 0.18814897537231445 сек; 0.09387016296386719 сек
# Время работы кода GB: 4.2028584480285645 с; 2.889289617538452 сек; 8.440896272659302 сек
