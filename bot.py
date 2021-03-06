# -*- coding: utf-8 -*-
import telebot
from telebot import types
import config
import main
from datetime import datetime


bot = telebot.TeleBot(config.TOKEN)


def log(message):
    date = str(datetime.now())
    string = (date + " FROM: " + message.from_user.first_name + ' '
          + message.from_user.last_name + ' USER_ID: ' + str(message.from_user.id) + ' MESSAGE: ' + message.text)
    f = open("./bot.log", 'a')
    f.write(string + '\n')
    f.close()


def driver_error(self):
    text = 'Здесь скоро будут решения проблем с установкой драйверов Рутокен'
    log(self)
    bot.send_message(self.chat.id, text)  # reply_markup = markup)


@bot.message_handler(commands=['start'])
def start(self):
    text = """Если тебе известен "Код ошибки" напиши его мне в формате "XX"\n\nЕсли возникли вопросы /help"""
    log(self)
    bot.send_message(self.chat.id, text)


@bot.message_handler(commands=['stop'])
def start(self):
    text = 'Уже уходишь? 😢\nЕсли понадоблюсь тебе ещё раз, пиши, помогу тебе в любой момент в любое время дня и ночи.'
    log(self)
    bot.send_message(self.chat.id, text)


@bot.message_handler(commands=['help'])
def help(self):
    text = """*Команды которые я понимаю*\n
/help - Помощь
/hotquestions - Часто задаваемые вопросы
/mailsupport - Обращение в департамент техподдержки\n
Все вопросы и пожелания пишите мне:
💬 Telegram - @ubushan
📩 Email - ubushaev08@gmail.com
📌 *З.Ы. В данный момент бот находится в состоянии разработки...*"""
    log(self)
    bot.send_message(self.chat.id, text, parse_mode="Markdown")


@bot.message_handler(commands=['mailsupport'])
def start(self):
    text = """*Обращение в департамент техподдержки:*\n\nЭта функция в разработке"""
    log(self)
    bot.send_message(self.chat.id, text, parse_mode="Markdown")


@bot.message_handler(commands=['hotquestions'])
def start(self):
    text = """*Часто задаваемые вопросы:*\n\nЭта функция в разработке"""
    log(self)
    bot.send_message(self.chat.id, text, parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def echo(self):
    log(self)
    bot.send_message(self.chat.id, main.parser(self.text), parse_mode="Markdown")


if __name__ == '__main__':
    bot.polling(none_stop=True)



    # print(type(self))
    # print(str(self.text))
    # print(self.text)
    # markup = types.ReplyKeyboardMarkup() # после обновления библиотеки telebot, кнопки перестали работать :(, пока не могу понять в чем проблема
    # markup.row('10', '37', '52', '1053')
    # markup.row('1060', '1111', '7777', '333')
    # markup.row('Назад')
    #bot.send_message(self.chat.id, self.text)  # reply_markup = markup)
    # if config.head.float_check(self.text):
    #     if self.text == self.text:
    #         #print(type(self.text)) # Вывод в консоль для проверки
    #     # else:
    #     #     bot.send_message(self.chat.id, 'Что-то пошло не так')
    # elif self.text == 'Назад':
    #     return start(self)
    # elif self.text == 'Прочие проблемы':
    #     return driver_error(self)
    # else:
    #     text = """Если тебе известен "Код ошибки" напиши его мне в формате XX"""
    #     #print(str(self.text))
    #     bot.send_message(self.chat.id, text)
    # return 'Что-то пошло не так :('