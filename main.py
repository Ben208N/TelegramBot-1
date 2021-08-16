# import os
# import telebot

# API_KEY = os.environ['API_KEY']
# bot = telebot.TeleBot(API_KEY)

# @bot.message_handler(commands=['Greet'])
# def greet(message):
#   bot.reply_to(message, "Hey! Hows it going?")

# @bot.message_handler(commands=['hello'])
# def hello(message):
#   bot.send_message(message.chat.id, "Hello!")

# bot.polling()

import telebot
import time

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

bot = telebot.TeleBot(token="1991530978:AAGOEJUqs3eK_p5SQz-UqXAzFXCxC-mxmug")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hey b")

@bot.message_handler(commands=['Timer'])
def timer(message):
    bot.reply_to(message, "For how long?")

@bot.message_handler(commands=['minutes'])
def minutes(message):
    bot.reply_to(message, "OK!")
    time.sleep(5.5)
    bot.reply_to(message, "ALERT!")



# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


bot.polling()
