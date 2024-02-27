"""
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print"""

MAX_NUMBER = 1000
MIN_NUMBER = 0
TENS = 10
HUNDREDS = 100


while True:
    number = int(input("Введите  число от 1 до 999: "))
    if MIN_NUMBER < number < MAX_NUMBER:
        if number < TENS:
            result = number**2
        elif number < HUNDREDS:
            result = (number // TENS) * (number % TENS)
        else:
            result = (
                number % TENS * HUNDREDS
                + number // TENS % TENS * TENS
                + number // HUNDREDS
            )
        break
print(result)


"""Ёлка из звездочек"""

# 1 вариант
def tree(rows: int):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))


tree(5)

# 2 вариант
height = int(input("Введите высоту ёлки: "))

for i in range(height):
    print(f'{"*" * (2 * i + 1):^{2 * height + 1}}')  # f строка с выравниванием


"""Таблица умножения"""
# 1 вариант
for k in [0, 4]:
    print()
    for i in range(2, 11):
        print()
        for j in range(2 + k, 6 + k):
            print(f"{j} * {i} = {i * j}\t", end="")


# 2 вариант в сроку
print(
    "\n\n".join(
        [
            "\n".join(
                [
                    "\t\t".join(
                        [f"{y:<2}* {x:<2} = {x*y:>2}" for y in range(2 + n, 6 + n)]
                    )
                    for x in range(2, 11)
                ]
            )
            for n in (0, 4)
        ]
    )
)
