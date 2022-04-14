from random import randint
import telebot
from requests import get
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('5376308598:AAFjtv5gTxPYoob4m0Ell-pfoNgJu51i4ig')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/Fox")
    item2 = types.KeyboardButton("/Cat")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Нажми: \n/Fox — для получения картинки лисы\n/Cat — для получения картинки котика ',
                     reply_markup=markup)


# Получение сообщений от пользователя
@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = ""
    # Если пользователь прислал 1, выдаем ему случайного кота
    if message.text.strip() == '/Cat':
        num = randint(1, 1000)
        source = get(f"https://aws.random.cat/view/{num}").text
        if "id=\"cat" in source:
            answer = source.split("src=\"")[1].split("\"")[0]
            bot.send_photo(message.chat.id, answer)
        else:
            print("Incorrect id")

    # Если пользователь прислал 2, выдаем случайную лису
    elif message.text.strip() == '/Fox':
        num = randint(1, 121)
        answer = f"https://randomfox.ca/images/{num}.jpg"
        bot.send_photo(message.chat.id, answer)

    else:
        answer = "Это не кот и не лиса"
        bot.send_message(message.chat.id, answer)

    #bot.send_photo(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=1)