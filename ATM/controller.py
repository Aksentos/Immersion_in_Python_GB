import view
import models
import text
import currency


def start_app():
    while True:
        user_choice = view.show_enter_menu()  # первое меню банкомата
        match user_choice:
            case 1:
                models.open_clients()
                user_pass = view.show_enter_password()
                if models.check_password(user_pass):  # работа со счетом клиента
                    name = models.check_password(user_pass)
                    view.show_message(text.greeting(name))
                    while True:
                        client_choice = view.show_main_menu()
                        match client_choice:
                            case 1:  # показать баланс
                                view.show_message(
                                    text.balance(
                                        models.clients[name][1],
                                        models.clients[name][3],
                                        models.clients[name][5],
                                    )
                                )
                            case 2:  # Снять наличные
                                take_off = view.show_withdraw()
                                if isinstance(take_off, int) and take_off <= float(
                                    models.clients[name][1]
                                ):
                                    commission = models.withdraw_cash(name, take_off)
                                    view.show_message(
                                        text.comission_withdrawal(commission)
                                    )
                                    adding = models.third_operation(name)
                                    if adding:
                                        view.show_message(text.add_bonus(adding))
                                    view.show_message(
                                        text.balance(
                                            models.clients[name][1],
                                            models.clients[name][3],
                                            models.clients[name][5],
                                        )
                                    )
                                else:
                                    view.show_message(text.withdraw_not_enought)
                                lux_tax = models.wealth_tax(name)
                                if lux_tax:
                                    view.show_message(text.luxury_tax(lux_tax))
                            case 3:  # Полонить счет
                                currensy_select = view.currency_selection()
                                
                                if isinstance(currensy_select, int):
                                    add = view.adding_money()
                                    if isinstance(add, float):
                                        models.top_up(name, currensy_select, add)
                                        view.show_message(text.adding_succesfully)
                                        adding = models.third_operation(name)
                                        if adding:
                                            view.show_message(text.add_bonus(adding))
                                        view.show_message(
                                            text.balance(
                                                models.clients[name][1],
                                                models.clients[name][3],
                                                models.clients[name][5],
                                            )
                                        )
                                    else:
                                        view.show_message(add)
                                else:
                                    view.show_message(currensy_select)
                                lux_tax = models.wealth_tax(name)
                                if lux_tax:
                                    view.show_message(text.luxury_tax(lux_tax))
                            case 4:  # Перевести деньги другому клиенту
                                pass
                            case 5:  # Конвертер валют
                                pass
                            case 6:  # выход + сохранение изменений баланса
                                models.save_client()
                                break

                else:
                    view.show_message(text.invalid_password)

            case 2:
                view.show_message(
                    text.currency(
                        text.euro,
                        currency.bank_curr(currency.cur_eur)[0],
                        currency.bank_curr(currency.cur_eur)[1],
                    )
                )
                view.show_message(
                    text.currency(
                        text.dollar,
                        currency.bank_curr(currency.cur_usd)[0],
                        currency.bank_curr(currency.cur_usd)[1],
                    )
                )
            case 3:
                break


