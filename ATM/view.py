import text

BOARD = "-"
MULTIPLICITY = 50  # кратность снятия наличных


def show_enter_menu() -> int:
    print("\n" + BOARD * 20)
    for k, v in text.enter_menu.items():
        print(BOARD, k, v, BOARD)
    print(BOARD * 20)
    while True:
        choice_enter_menu = text.choice_menu(text.enter_menu)
        if choice_enter_menu.isdigit() and 0 < int(choice_enter_menu) <= len(
            text.enter_menu
        ):
            return int(choice_enter_menu)
        print(text.mistake_input)


def show_enter_password() -> int:
    password = input(text.enter_password)
    if password.isdigit() and len(password) == 4:
        return password
    return text.mistake_input


def show_message(message: str):
    print("\n" + BOARD * len(message))
    print(message)
    print(BOARD * len(message))


def show_main_menu() -> int:
    print("\n" + BOARD * 20)
    for k, v in text.main_menu.items():
        print(BOARD, k, v, BOARD)
    print(BOARD * 20)
    while True:
        choice_menu = text.choice_menu(text.main_menu)
        if choice_menu.isdigit() and 0 < int(choice_menu) <= len(text.main_menu):
            return int(choice_menu)
        print(text.mistake_input)


def show_withdraw() -> int | str:
    quantity = input(text.withdraw)
    if quantity.isdigit() and not float(quantity) % MULTIPLICITY:
        return int(quantity)
    return text.mistake_input


def currency_selection() -> int:
    currency = input(text.curr_select)
    if currency.isdigit() and 0 < int(currency) < 4:  # нужно будет поменять на динамическое сравнение
        return int(currency)
    return text.mistake_input


def adding_money():
    add = input(text.adding)
    if add.isdigit():
        return float(add)
    return text.mistake_input