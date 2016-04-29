# -*- coding: utf-8 -*-
import csv


TOKEN = '186044924:AAHUcAUHTg-gjgZMylRgmD4tUYl2t94AzcQ'
PATH_DATA = 'C:\\Users\\Ubushaev\\PycharmProjects\\aktiv\\data\\' # Это путь локального каталога расположенного на моем рабочем компе.


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


    def error(self): # старый парсер по файлу errorcode.csv, его можно использовать в дополнительных целях, если нужно
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


    def search_kb(self): # актуальный на данный момент парсер 29/04/16
        url = SITE + "/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "&queryString=" + self
        html_doc = urlopen(url).read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        # text = (soup.find_all('div', 'highlights'))
        for link in soup.find_all('a', 'search-result-link visitable'):
            content = SITE + link.get('href')
            return [content]