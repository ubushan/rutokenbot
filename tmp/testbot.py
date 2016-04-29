import telebot
import config
import time
from telebot import types

#bot = telebot.TeleBot(config.TOKEN)

tb = telebot.AsyncTeleBot(config.TOKEN)

task = tb.get_me() # Execute an API call
# Do some other operations...
a = 0
for a in range(100):
    a += 10

result = task.wait()


bot.polling(none_stop=True)

while True:
    time.sleep(20)