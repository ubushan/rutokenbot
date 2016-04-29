# -*- coding: utf-8 -*-
import csv
import re

TOKEN = '186044924:AAHUcAUHTg-gjgZMylRgmD4tUYl2t94AzcQ'
PATH_DATA = 'C:\\Users\\Ubushaev\\PycharmProjects\\aktiv\\data\\'  # На данный момент 29/04/16 этот путь уже не актуален, т.к. бот парсит сайт

from urllib.request import urlopen
from bs4 import BeautifulSoup

SITE = 'http://kb.rutoken.ru'


class head():
    def float_check(self):
        try:
            float(self)
            return True
        except ValueError:
            return False

    def error(self):  # старый парсер по файлу errorcode.csv, его можно использовать в дополнительных целях, если нужно
        if self:
            with open(PATH_DATA + "errorcode.csv", 'r') as csvfile:
                fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
                csvfile.seek(0)
                empty = {}
                dictReader = csv.DictReader(csvfile, dialect=fileDialect)
                for row in dictReader:
                    empty[row['Code'].replace('Код ошибки: ', '')] = row['Error']
                return empty[self]
        else:
            return 'Такого кода ошибки в моей Базе Знаний нет :('

    # def search_kb(self): # старый кривой парсер
    #     url = "http://developer.rutoken.ru/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "&queryString=" + self
    #     html_doc = urlopen(url).read()
    #     soup = BeautifulSoup(html_doc, 'html.parser')
    #     text = (soup.find('ol', 'search-results cql'))
    #     #link = (soup.find('a', 'search-result-link'))
    #     return (text.get_text() + '\n')


    def search_kb(self):
        url = SITE + "/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "&queryString=" + self
        html_doc = urlopen(url).read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        check = soup.find_all('div', 'search-results-container')
        notresult = re.findall(r'No results found for', str(check))
        yesresult = re.findall(r'data-totalsize', str(check))
        if yesresult[0] == 'data-totalsize':
            lst = []
            for link in soup.find_all('a', 'search-result-link visitable'):
                content = SITE + link.get('href')
            for descript in soup.find_all('div', 'highlights'):
                text = descript.get_text('')
                lst.append('- ' + text[:120] + '... ' + '\nУзнать подробнее: ' + content + ' \n')
                a = str(lst)
                b = re.sub(r"\['|\']|', '", '', a)
                c = re.sub(r"\\n", '\n', b)
                d = re.sub(r"- ", '\n- ', c)
            return ('Результаты поиска:' + '\n' + d + '\n- - -'
                                                   '\nЕсли не нашел решение проблемы, напиши нам!'
                                                   '\nhotline@rutoken.ru - Техническая поддержка')
        elif notresult[0] == 'No results found for':
            return 'По вашему запросу ничего не найдено'
        else:
            return 'Что-то пошло не так :('