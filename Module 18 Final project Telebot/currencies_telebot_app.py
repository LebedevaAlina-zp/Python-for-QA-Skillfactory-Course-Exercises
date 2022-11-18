import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message: telebot.types.Message):
    text = '''Это бот-калькулятор конвертации валют. Введите команду в формате:
    <валюта, из которой переводим> <валюта, в которую переводим> <сумма в первой валюте>
    Например: доллар рубль 100
    Посмотреть список досутпных валют можно по команде /values'''
    bot.send_message(message.chat.id, text)

    
bot.polling(none_stop=True)
