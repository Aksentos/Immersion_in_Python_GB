""" Задание №1
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""


# var 1
def split_text(text: str) -> None:
    text = text.split()
    max_len = len(max(text, key=len))

    for i, item in enumerate(sorted(text), 1):
        print(f"{i}. {item:>{max_len}}")


# var 2
def func_string(srtn: str):
    strn = sorted(srtn.lower().split())
    max_len = len(max(strn, key=len))
    for num, word in enumerate(strn, 1):
        print(f"{num} {word:>{max_len}}")


"""Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


# var 1
def char_ord(string: str) -> list[int]:
    return sorted(set([ord(i) for i in string]), reverse=True)


print(char_ord("asdag"))


# var 2
def str_text(text: str) -> list[int]:
    cod = sorted(set(ord(i) for i in text), reverse=True)
    return cod


text = "Всем привет кто смотрит респект"
print(str_text(text))

"""Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


# var 1
def unic_number(string: str) -> dict:
    my_list = [int(x) for x in string.split()]
    uni = {}
    for i in range(min(my_list), max(my_list) + 1):
        uni[chr(i)] = i
    return uni


# var 2
def uni_dict(some_str: str) -> dict[str, int]:
    min_num, max_num = sorted(map(int, some_str.split()))
    return {chr(i): i for i in range(min_num, max_num + 1)}


"""Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""


# var 1
# сортировка пузырьком
def sort_numbers(numbers: list[int]) -> list[int]:
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


print(sort_numbers([1, 5, 6, 77, 3]))


# var 2
def sorts_list(lst: list, *, reverse=False):
    for _ in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if reverse:
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst


my_liast = [10, 12, 8, 10, 2, 3, 11, 5]
sorts_list(my_liast, reverse=True)
print(my_liast)

"""Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""
name = ["Максим", "Андрей", "Сергей", "Пётр"]
bet = [50000, 49000, 20000, 15000]
prize = ["13.25%", " 13.42%", "10.20%", "15.3%"]


# var 1
def prizes(names: list, moneys: list, bonuses: list) -> dict:
    answer = {}
    for nam, money, bonus in zip(names, moneys, bonuses):
        answer[nam] = money * float(bonus[:-1]) * 0.01
    return answer


print(prizes(name, bet, prize))


# var 2
def work_salary(name, bet, prize):
    my_dict = {}
    for index, item in enumerate(name):
        my_dict[item] = bet[index] + (
            bet[index] / 100 * float(prize[index].replace("%", ""))
        )
    return my_dict


# var 3
def prizes(names: list, moneys: list, bonuses: list) -> dict:
    return {
        nam: money * float(bonus[:-1]) * 0.01
        for nam, money, bonus in zip(names, moneys, bonuses)
    }


"""Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""
from random import randint


# var 1
def summ_srez(numbers: list[int], index_1: int, index_2: int) -> int:
    if index_1 < index_2:
        return sum(numbers[index_1 + 1 : index_2])
    else:
        return sum(numbers[index_2 + 1 : index_1])


nums = [randint(1, 100) for _ in range(10)]
num1 = randint(0, 10)
num2 = randint(0, 100)

print(summ_srez(nums, num1, num2))


# var 2
def sum_list_nums(list_nums, a, b) -> int:
    if a > b and a > 0 > b:
        return sum(list_nums[a:b:-1])
    elif b < a < 0:
        return sum(list_nums[a:b:-1])
    else:
        return sum(list_nums[a:b])


print(sum_list_nums([2, 5, 2, 6, 8, 4], -2, -4))


# var 3
def list_index_sum(lists, index_1, index_2) -> int:
    if index_1 > len(lists) or index_1 < 0:
        index_1 = 0
    return sum(lists[index_1:index_2])


"""Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь
"""

my_dict = {
    "Яндекс": ([50, 10, 20], [1, 10, 5, 8]),
    "Google": ([20, 18, 55], [8, 14, 17]),
    "Mail": ([80, 51, 13], [7, 16, 20]),
    "Вконтакте": ([17, 46, 20, 55], [13, 18, 77]),
}


# var 1
def company(companyes: dict) -> bool:
    result = []
    for v in companyes.values():
        result.append(True if (sum(v[0]) - sum(v[1])) > 0 else False)
    return all(result)


print(company(my_dict))


# var 2
def total_profit(dicts):
    gain = []
    company_finances = []
    for name, value in dicts.items():
        debit = sum(value[0]) - sum(value[1])
        gain.append(debit)
        company_finances.append((name, debit))
    return company_finances, all(map(lambda x: x > 0, gain))


# var 3
def test_companies(dict_companies):
    return all([sum(dict_companies[key]) > 0 for key in dict_companies.keys()])


# var 4
def check_profit(data: dict) -> bool:
    for values in data.values():
        if sum(values[0]) < sum(values[1]):
            return False
    return True


"""Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""
numbers = 123
text = "123123"
names = "Андрей"
s = "Python"


# var 1
def replase_value():
    for i in list(globals()):
        if i.endswith("s") and i != "s":
            globals()[i[:-1]] = globals()[i]
            globals()[i] = None
    return list(filter(lambda x: not x[0].startswith("__"), globals().items()))


print(*replase_value(), sep="\n")


# var 2
def rename_variable():
    temp = {}
    for key, value in globals().items():
        if key.endswith("s") and len(key) > 1:
            temp[key[:-1]] = value
            temp[key] = None
    print(temp)
    globals().update(temp)
