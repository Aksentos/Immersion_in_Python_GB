main_menu = {
    1: "Показать баланс",
    2: "Снять наличные",
    3: "Полонить счет",
    4: "Перевести деньги другому клиенту (в разработке)",
    5: "Конвертер валют (в разработке)",
    6: "Выход",
}

enter_menu = {1: "Вставьте карту", 2: "Курс валют    ", 3: "Выход         "}
enter_password = "Введите пин-код карты (4 цифры):\n  →"
mistake_input = "Неверный ввод, попробуйте снова!"
invalid_password = "Вы ввели неверный пароль или такого клинета нет!"
withdraw = "Введите сумму для снятия (кратную 50): "
withdraw_not_enought = "На счете не хватает средств или введена неверная сумма!"
curr_select = 'Какую валюту будете вносить? Введите 1 - рубли (₽), 2 - доллары ($), 3 - евро (€): '
adding = 'Введите сумму которую хотите внести на счет: '
adding_succesfully = "Деньги внесены успешно!"

euro = "€"
dollar = "$"


def currency(cur_name, price_buy: float, price_sell: float) -> str:
    return f"Курс 1 {cur_name}: покупка {price_buy} ₽, продажа {price_sell} ₽"


def greeting(name: str) -> str:
    return f"Добро пожаловать {name}! \nВыберите действие"


def choice_menu(menu: dict) -> str:
    choice = input(f"Выберите пункт меню (от 1 до {len(menu)}): ")
    return choice


def balance(rub, usd, eur) -> str:
    return f"У вас на счете: {rub} ₽, {usd} $, {eur} €"


def comission_withdrawal(commisson: float) -> str:
    return f"Комиссия за снятие наличных составила: {commisson} ₽"


def add_bonus(adding_bonus) -> str:
    return f"Вам начислено {adding_bonus} ₽, спасибо что пользуетесь нашими услугами!"

def luxury_tax(tax: float) -> str:
    return f'Начислен налог {tax} ₽!'
