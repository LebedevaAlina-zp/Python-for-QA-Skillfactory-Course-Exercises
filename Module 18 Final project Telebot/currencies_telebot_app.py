import requests
import telebot
import json
from extensions import APIException
from config import TOKEN, currencies

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message: telebot.types.Message):
    text = '''Это бот-калькулятор конвертации валют. Введите команду в формате:
    <валюта, в которую переводим> <валюта, из которой переводим> <количество первой валюты>
    Например: доллар рубль 100
    Посмотреть список досутпных валют можно по команде /values'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def handle_values(message: telebot.types.Message):
    text = ''
    for key in currencies.keys():
        text = '\n'.join((text, key))
    text = f"Список доступных валют:\n {text}"
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def curr_converter(message: telebot.types.Message):
    params = message.text.split()

    if len(params) != 3:
        raise APIException("Команда должна содержать ровно 3 параметра.")

    quote, base, amount = params

    r = requests.get(f'https://api.exchangerate.host/convert?from={currencies[quote]}&to={currencies[base]}')
    total_base = r.json()['result'] * float(amount)
    text = f"{amount} {quote} - это {total_base} {base} по курсу https://exchangerate.host"

    bot.reply_to(message, text)


bot.polling(none_stop=True)
