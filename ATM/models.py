import currency

clients = {}  # база данных клиентов

path = "users.txt"
SEPARATOR = ";"

COMMISSION_WITHDRAWAL = 0.015
MIN_COMMISSION_WITHDRAWAL = 30
MAX_COMMISSION_WITHDRAWAL = 600
OPERATIONS_NUMBER = 3
BONUS = 0.03
WEALTH = 5_000_000


def open_clients():
    global clients
    with open(path, "r", encoding="UTF-8") as users:
        data = users.readlines()
    for user in data:
        user = user.strip().split(SEPARATOR)
        clients[user[0]] = user[1:]


def save_client():
    global clients
    data = [k + ";" + ";".join(v) for k, v in clients.items()]
    data = "\n".join(data)
    with open(path, "w", encoding="UTF-8") as base:
        base.write(data)


def check_password(password: str):
    global clients
    for name, info in clients.items():
        if password in info:
            return name
    return False


def withdraw_cash(user: str, withdraw: int) -> float:
    global clients

    if withdraw * COMMISSION_WITHDRAWAL < MIN_COMMISSION_WITHDRAWAL:
        clients[user][1] = str(
            float(clients[user][1]) - withdraw - MIN_COMMISSION_WITHDRAWAL
        )
        return MIN_COMMISSION_WITHDRAWAL
    elif withdraw * COMMISSION_WITHDRAWAL < MAX_COMMISSION_WITHDRAWAL:
        clients[user][1] = str(
            float(clients[user][1]) - withdraw - withdraw * COMMISSION_WITHDRAWAL
        )
        return withdraw * COMMISSION_WITHDRAWAL
    else:
        clients[user][1] = str(
            float(clients[user][1]) - withdraw - MAX_COMMISSION_WITHDRAWAL
        )
        return MAX_COMMISSION_WITHDRAWAL


def third_operation(user: str) -> str:
    global clients
    clients[user][7] = str(int(clients[user][7]) + 1)
    if not int(clients[user][7]) % OPERATIONS_NUMBER:
        adding = round(float(clients[user][1]) * BONUS, 2)
        clients[user][1] = str(round(float(clients[user][1]) + adding, 2))
        return adding
    return False


def top_up(user: str, currency: int, adding: float):
    global clients
    if currency == 1:
        clients[user][1] = str(float(clients[user][1]) + adding)
    elif currency == 2:
        clients[user][3] = str(float(clients[user][3]) + adding)
    elif currency == 3:
        clients[user][5] = str(float(clients[user][5]) + adding)


def wealth_tax(user: str):
    global clients
    cost = (
        float(clients[user][1])
        + float(clients[user][3]) * currency.cur_usd
        + float(clients[user][5]) * currency.cur_eur
    )
    if cost > WEALTH:
        clients[user][1] = str(round(float(clients[user][1]) - cost / 10, 2))
        return round(cost / 10, 2)
    return False
