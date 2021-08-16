# import os
# import telebot

# API_KEY = os.environ['API_KEY']
# bot = telebot.TeleBot(API_KEY)


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
