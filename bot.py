# -*- coding: utf-8 -*-
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)


def driver_error(self):
    text = 'Здесь скоро будут решения проблем с установкой драйверов Рутокен'
    bot.send_message(self.chat.id, text)  # reply_markup = markup)


def code_error(self):
    return config.head.search_kb(self)


@bot.message_handler(commands=['start'])
def start(self):
    text = 'Привет, если тебе известен "Код ошибки" скажи его мне в формате "XX".\n' \
           '\nПоказать все команды бота /help'
    bot.send_message(self.chat.id, text)


@bot.message_handler(commands=['stop'])
def start(self):
    text = 'Пока :('
    bot.send_message(self.chat.id, text)


@bot.message_handler(commands=['help'])
def help(self):
    text = 'Команды которые я понимаю\n' \
           '/help - Помощь\n\n' \
           'Все вопросы и пожелания пишите мне:\n' \
           'Telegram - @ubushan\n' \
           'Email - ubushaev08@gmail.com\n\n' \
           'З.Ы. В данный момент бот находится в состоянии разработки...'
    bot.send_message(self.chat.id, text)


@bot.message_handler(func=lambda msg: True)
def echo(self):
    # markup = types.ReplyKeyboardMarkup()
    # markup.row('10', '37', '52', '1053')
    # markup.row('1060', '1111', '7777', '333')
    # markup.row('Назад')
    bot.send_message(self.chat.id, self.text)  # reply_markup = markup)
    if config.head.float_check(self.text):
        if self.text == self.text:
            bot.send_message(self.chat.id, code_error(self.text))
        else:
            bot.send_message(self.chat.id, 'Что-то пошло не так')
    elif self.text == 'Назад':
        return start(self)
    elif self.text == 'Прочие проблемы':
        return driver_error(self)
    else:
        bot.send_message(self.chat.id, 'Выберите "Код ошибки" из списка или введите в формате "XX"!')


if __name__ == '__main__':
    bot.polling(none_stop=True)