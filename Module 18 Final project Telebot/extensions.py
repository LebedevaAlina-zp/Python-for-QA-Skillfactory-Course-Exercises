import requests
import json
from config import currencies, dollar_names, euro_names, ruble_names

class APIException(Exception):
    pass


class CurrenciesConversion():
    @staticmethod
    def conversion(base: str, quote: str, amount: str):
        try:
            base_code = currencies[base.lower()]
        except KeyError:
            if base.lower() in dollar_names: # проверим, не указал ли пользователь одно из альтернативных названий валюты
                base_code = currencies['доллар']
            elif base.lower() in euro_names:
                base_code = currencies['евро']
            elif base.lower() in ruble_names:
                base_code = currencies['рубль']
            else:
                raise APIException(f"Не удалось обработать валюту <{base}>.\nСписок доступных валют можно проверить по команде /values")

        try:
            quote_code = currencies[quote.lower()]
        except KeyError:
            if quote.lower() in dollar_names:  # проверим, не указал ли пользователь одно из альтернативных названий валюты
                quote_code = currencies['доллар']
            elif quote.lower() in euro_names:
                quote_code = currencies['евро']
            elif quote.lower() in ruble_names:
                quote_code = currencies['рубль']
            else:
                raise APIException(f"Не удалось обработать валюту <{quote}>.\nСписок доступных валют можно проверить по команде /values")

        try:
            amount = float(amount.replace(',', '.')) # если пользователь ввел разделительную запятую вместо точки
        except ValueError:
            raise APIException(f"Не удалось обработать сумму {amount}.")

        r = requests.get(f'https://api.exchangerate.host/convert?from={base_code}&to={quote_code}')
        total_base = r.json()['result'] * amount

        return total_base

