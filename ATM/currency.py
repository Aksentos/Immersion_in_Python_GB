import requests
from bs4 import BeautifulSoup


""" Доделать парсинг валют на текущий день!!!"""


def today_currency():
    url = "https://cbr.ru/currency_base/daily/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0"
    }
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    all_currencies = soup.findAll("td")

    for ids, currence in enumerate(all_currencies):
        if "USD" in currence:
            cur_usd = (
                str(all_currencies[ids + 3]).replace("<td>", "").replace("</td>", "")
            )
        if "EUR" in currence:
            cur_eur = (
                str(all_currencies[ids + 3]).replace("<td>", "").replace("</td>", "")
            )
    return cur_usd, cur_eur


cur_usd = float(today_currency()[0].replace(",", "."))
cur_eur = float(today_currency()[1].replace(",", "."))


def bank_curr(currency: float) -> list:
    bank_buy = round(currency * 0.98, 2)
    bank_sell = round(currency * 1.03, 2)
    return [bank_buy, bank_sell]
