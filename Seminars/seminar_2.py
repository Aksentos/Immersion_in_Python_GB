'''
Задание №1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
'''
number = 11
bl = True
string = 'Строка'
f_number = 3.14
nont = None

print(type(number))
print(type(bl))
print(type(string))
print(type(f_number))
print(type(nont))


"""Задание №2
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты."""

import sys

data = [1, True, 3.14, "string", 23, "string", -1]

print(
    *[
        (
            f"порядковый номер: {i}",
            f"значение: {v}",
            f"адрес в памяти: {id(v)}",
            f"размер в памяти: {v.__sizeof__()}",
            f"хэш объекта: {hash(v)}",
        )
        for i, v in enumerate(data, 1)
    ],
    sep="\n",
)


# 2 вариант
for index, value in enumerate(data, 1):
    print(f'порядковый номер:{index}')
    print(f"значение:{value}")
    print(f'адрес в памяти:{id(value)}')
    print((f'размер в памяти:{sys.getsizeof(value)}'))
    print(f'хэш объекта:{hash(value)}')

    if isinstance(value, int) and value > 0:
        print(f'результат проверки на целое число: True')
    else:
        print(f'результат проверки на целое число: False')

    if isinstance(value, str):
        print(f'результат проверки на на строку: True')
    else:
        print(f'результат проверки на на строку: False')
    print('\n',"=="*40)

"""Задание №3
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно"""

BIN = 2
OCT = 8

number = int(input("Введите число: "))

# 1 вариант
string = ""
while number != 0:
    string = str(number % BIN) + string
    number //= BIN
print("0b" + string)


# 2 вариант
def num_to_base(orig_number: int, base: int):
    result = ""
    while orig_number != 0:
        result = str(orig_number % base) + result
        orig_number //= base
    return result


print("0b" + num_to_base(number, BIN))
print(bin(number))
print("0o" + num_to_base(number, OCT))
print(oct(number))


'''Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
'''
import decimal
import math


diametr = float(input('Введите диаметр'))
decimal.getcontext().prec = 42
s = decimal.Decimal(math.pi) * (decimal.Decimal(diametr)/2)**2
p = 2 * decimal.Decimal(math.pi) * decimal.Decimal(diametr)/2
print(f'Площадь = {s}', f'Длина окружности = {p}', sep='\n')


"""Задание №5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня."""

a, b, c = 2.1, 3.14, 5.6
d = b**2 - 4 * a * c
x1 = (-b + d**0.5)/(2*a)
x2 = (-b - d**0.5)/(2*a)
print(f'первый корень: {x1}, второй корень: {x2}')


'''Задание №6* (решаем сами)
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''

