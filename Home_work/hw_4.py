"""Транспонирование матрицы
Напишите функцию для транспонирования матрицы transposed_matrix,
принимает в аргументы matrix, и возвращает транспонированную матрицу.
"""

"""ВАЖНО!!! GB тесты не принимают аннотацию, её писать не надо! """


# var 1
def transpose(matrix):
    transp_matrix = []
    # создаем новую пустую матрицу с обратным количеством строк и столбцов
    for i in matrix:
        for _ in range(len(i)):
            transp_matrix.append([])
        break
    # заполняем новую матрицу значениями из старой
    for i in matrix:
        for j in range(len(i)):
            transp_matrix[j].append(i[j])
    return transp_matrix


print(transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))


# var 2 GB
def transpose(matrix):
    # определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # создаем новую матрицу с размерами, поменянными местами
    transposed = [[0 for row in range(rows)] for col in range(cols)]

    # заполняем новую матрицу значениями из старой матрицы
    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]

    return transposed


"""Преобразование ключей и значений словаря
Напишите функцию key_params, принимающую на вход только ключевые параметры и
возвращающую словарь, где ключ - значение переданного аргумента, а значение -
имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


# var 1
def key_params(**kwargs):
    my_dict = {}
    for k, v in kwargs.items():
        try:
            hash(v)
            my_dict[v] = k
        except TypeError:
            my_dict[str(v)] = k
    return my_dict


params = key_params(a=1, b="hello", c=[1, 2, 3], d={})
print(params)


# var 2 GB
def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value is None:
            result[value] = key
        elif isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result


"""Задача о банкомате
У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять 
этой картой, выполняя следующие операции, для выполнения которых необходимо написать 
следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных 
операциях.

Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. 
Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.

Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия 
также должна быть кратной MULTIPLICITY. При снятии средств начисляется комиссия в 
процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:
Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету 
больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю 
MULTIPLICITY. Реализуйте программу для управления банковским счетом, используя библиотеку
decimal для точных вычислений.
"""


import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

"""мое решение, его автотест GB не принимает!!!"""
def check_multiplicity(amount):
    if not amount % MULTIPLICITY:
        return amount
    print("Сумма должна быть кратной 50 у.е.")
    return False


def deposit(amount):
    global bank_account, operations, count
    introduction = check_multiplicity(amount)
    if introduction:
        bank_account += decimal.Decimal(introduction)
        operations.append(
            f"Пополнение карты на {introduction} у.е. Итого {bank_account} у.е."
        )
        count += 1


def withdraw(amount):
    global bank_account, operations, count
    wd = check_multiplicity(amount)
    if wd:
        removal = decimal.Decimal(wd) * PERCENT_REMOVAL
        if removal < MIN_REMOVAL:
            removal = MIN_REMOVAL
        elif removal > MAX_REMOVAL:
            removal = MAX_REMOVAL

        if wd + removal <= bank_account:
            bank_account -= decimal.Decimal(wd) + removal
            operations.append(
                f"Снятие с карты {wd} у.е. Процент за снятие {int(removal)} у.е.. Итого {bank_account} у.е."
            )
            count += 1
        else:
            operations.append(
                f"Недостаточно средств. Сумма с комиссией {int(wd+removal)} у.е. На карте {bank_account} у.е."
            )


def exit():
    global bank_account, operations, count
    if bank_account > RICHNESS_SUM:
        tax = bank_account * RICHNESS_PERCENT
        bank_account -= tax
        operations.append(
            f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax} у.е. Итого {bank_account} у.е."
        )
    operations.append(f"Возьмите карту на которой {bank_account} у.е.")


# решение GB для автотеста!:
def check_multiplicity(amount):
    """Проверка кратности суммы"""
    if (amount % MULTIPLICITY) != 0:
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
        return False
    return True


def deposit(amount):
    """Пополнение счета"""
    global bank_account, count
    if not check_multiplicity(amount):
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
        return False  # Операция не выполнена из-за некратной суммы
    count += 1
    bank_account += amount
    operations.append(f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е.")
    return True


def withdraw(amount):
    """Снятие денег"""
    global bank_account, count
    percent = amount * PERCENT_REMOVAL
    percent = (
        MIN_REMOVAL
        if percent < MIN_REMOVAL
        else MAX_REMOVAL
        if percent > MAX_REMOVAL
        else percent
    )
    if bank_account >= amount + percent:
        count += 1
        bank_account = bank_account - amount - percent
        operations.append(
            f"Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Итого {int(bank_account)} у.е."
        )
    else:
        operations.append(
            f"Недостаточно средств. Сумма с комиссией {amount + int(percent)} у.е. На карте {int(bank_account)} у.е."
        )


def exit():
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        percent = bank_account * RICHNESS_PERCENT
        bank_account -= percent
        operations.append(
            f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {percent} у.е. Итого {bank_account} у.е."
        )
    operations.append(f"Возьмите карту на которой {bank_account} у.е.")
