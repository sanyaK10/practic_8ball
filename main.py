import telebot
import os
from dotenv import load_dotenv
import random

load_dotenv()

TOKEN = os.getenv('TOKEN')

if TOKEN is None:
    print('Token is not found!')
    exit()


bot = telebot.TeleBot(TOKEN)
answers = ["так","ні"]

@bot.message_handler(commands=['start', 'help', 'qwerty'])
def send_welcome(message):
    print(type(message))
    bot.reply_to(message, 'Привіт, я 8ball-бот! Постав мені питання на яке відповідь так або ні і я видам магічний прогноз!')

@bot.message_handler(commands=['info'])
def send_info(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_name = message.from_user.username
    user_id = message.from_user.id
    chat_id = message.chat.id
    msg_text = message.text

    print(first_name, last_name, user_name, user_id, chat_id, msg_text)

    reply_msg = f"Привіт, {first_name}\n" \
                f"Твій Telegram ID: {user_id}\n" \
                f"Твоє повідомлення: {msg_text}\n"
    
    bot.reply_to(message, reply_msg)
    bot.send_message(374467027, reply_msg)

@bot.message_handler(func=lambda message: message.text.startswith('hello'))
def hello_answer(message):
    bot.send_message(message.chat.id, 'Привіт!')
    if "?" in message.text:
        bot.send_message(message.chat.id, random.choice(answers))
    else:
        bot.send_message(message.chat.id, "Постав питання зі знаком ?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, random.choice(answers))

if __name__ == "__main__":
    print('Bot is running...')
    bot.infinity_polling()






















































#     import telebot
# import os
# import random
# import string
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv('TOKEN')

# if TOKEN is None:
#     print('Token is not found!')
#     exit()

# bot = telebot.TeleBot(TOKEN)

# answers = [
#     'Так',
#     'Ні',
#     'Можливо',
#     'Без сумніву',
#     'Запитай пізніше',
#     'Дуже ймовірно'
# ]

# symbols = string.ascii_letters + string.digits + '!@#$%'


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(
#         message,
#         'Привіт, я бот!\n'
#         'Напиши питання — Magic 8 Ball 🎱\n'
#         'Напиши число — генератор пароля 🔐'
#     )


# @bot.message_handler(commands=['info'])
# def send_info(message):
#     first_name = message.from_user.first_name
#     user_id = message.from_user.id
#     msg_text = message.text

#     reply_msg = f"Привіт, {first_name}\n" \
#                 f"Твій ID: {user_id}\n" \
#                 f"Твоє повідомлення: {msg_text}"

#     bot.reply_to(message, reply_msg)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     text = message.text

#     if text.isdigit():
#         password = ''.join(random.choice(symbols) for _ in range(int(text)))
#         bot.send_message(message.chat.id, password)
#     else:
#         bot.send_message(message.chat.id, random.choice(answers))


# if __name__ == "__main__":
#     print('Bot is running...')
#     bot.infinity_polling()