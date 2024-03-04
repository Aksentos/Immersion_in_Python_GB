'''
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
'''

HEX = 16
num = int(input('Введите целое число'))

def num_to_base(orig_number: int, base: int):
    h = '0123456789ABCDEF'
    result = ""
    while orig_number != 0:
        remains = orig_number % base
        for i, num in enumerate(h):
            if remains == i:
                result = num + result
        orig_number //= base
    return result

print(f'Шестнадцатеричное представление числа: {num_to_base(num, HEX)}')
print(f'Проверка результата: {hex(num)}')

"""
Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions.
"""

import fractions

a = input('Введите первую дробь вида "1/2": ').split("/")
b = input('Введите вторую дробь вида "1/2": ').split("/")
a1 = fractions.Fraction(int(a[0]), int(a[1]))
b1 = fractions.Fraction(int(b[0]), int(b[1]))


def frac_summ(a: str, b: str) -> str:
    result = []

    if a[1] == b[1]:
        result.append(int(a[0]) + int(b[0]))
        result.append(int(a[1]))
    else:
        result.append(int(a[0]) * int(b[1]) + int(b[0]) * int(a[1]))
        result.append(int(a[1]) * int(b[1]))

    if not int(result[0]) % int(result[1]):
        return f"{int(result[0]/result[1])}"

    # добавить проверку если дробь можно сократить
    return f"{result[0]}/{result[1]}"


def mult_frac(a: str, b: str) -> str:
    return f"{int(a[0])*int(b[0])}/{int(a[1])*int(b[1])}"


print(f"Сумма = {frac_summ(a, b)}", f"Проверка суммы {a1 + b1}", sep="\n")
print(f"Произведение = {mult_frac(a, b)}", f"Проверка произведения {a1 * b1}", sep="\n")
