import requests
#import json
from config import currencies, dollar_names, euro_names, ruble_names

class APIException(Exception):
    pass


def alt_curr_name(name: str):
    """Функция пытается исправить название валюты, чтобы представить ее в то же виде, в каком валюты записаны в ключах с
    ловаря currencies"""
    name = name.lower()
    if name in currencies.keys():
        return name
    if name in dollar_names:
        return 'доллар'
    elif name in euro_names:
        return 'евро'
    elif name in ruble_names:
        return 'рубль'
    else:
        return name


class CurrenciesConversion():
    @staticmethod
    def conversion(base: str, quote: str, amount: str):
        base = alt_curr_name(base)
        try:
            base_code = currencies[base][0]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту <{base}>.\nСписок доступных валют можно проверить по команде /values")

        quote = alt_curr_name(quote)
        try:
            quote_code = currencies[quote][0]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту <{quote}>.\nСписок доступных валют можно проверить по команде /values")

        try:
            # Преобразовываем строку в число, исправив возможную ошибку пользователя десятичный разделитель запятую
            # и отрицательную сумму
            amount = abs(float(amount.replace(',', '.'))) # если вдруг пользователь ввел разделительную запятую вместо точки
        except ValueError:
            raise APIException(f"Не удалось обработать сумму {amount}.")

        r = requests.get(f'https://api.exchangerate.host/convert?from={base_code}&to={quote_code}')
        total_base = r.json()['result'] * amount

        return round(total_base, 2), currencies[base][1], currencies[quote][1], amount
