# -*- coding: utf-8 -*-
#import csv
import re

TOKEN = '186044924:AAHUcAUHTg-gjgZMylRgmD4tUYl2t94AzcQ'
#PATH_DATA = 'C:\\Users\\Ubushaev\\PycharmProjects\\aktiv\\data\\'  # На данный момент 29/04/16 этот путь уже не актуален, т.к. бот парсит сайт

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

    # def error(self):  # старый парсер по файлу errorcode.csv, его можно использовать в дополнительных целях, если нужно
    #     if self:
    #         with open(PATH_DATA + "errorcode.csv", 'r') as csvfile:
    #             fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
    #             csvfile.seek(0)
    #             empty = {}
    #             dictReader = csv.DictReader(csvfile, dialect=fileDialect)
    #             for row in dictReader:
    #                 empty[row['Code'].replace('Код ошибки: ', '')] = row['Error']
    #             return empty[self]
    #     else:
    #         return 'Такого кода ошибки в моей Базе Знаний нет :('

    # def search_kb(self): # старый кривой парсер
    #     url = "http://developer.rutoken.ru/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "&queryString=" + self
    #     html_doc = urlopen(url).read()
    #     soup = BeautifulSoup(html_doc, 'html.parser')
    #     text = (soup.find('ol', 'search-results cql'))
    #     #link = (soup.find('a', 'search-result-link'))
    #     return (text.get_text() + '\n')


    def search_kb(self):
        url = SITE + "/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "+and+type+%3D+" + "page" + "&queryString=" + self
        html_doc = urlopen(url).read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        check = soup.find_all('div', 'search-results-container')
        count = soup.find_all('p', 'search-results-count')
        count2 = re.findall(r'\Showing \d* ', str(count))
        count3 = re.findall(r' \d* ', str(count2))
        print(count3[0])
        result = re.findall(r'data-totalsize', str(check))
        if bool(result) == True:
            lst = []
            for link in soup.find_all('a', 'search-result-link visitable'):
                content = SITE + link.get('href')
            for descript in soup.find_all('div', 'highlights'):
                text = descript.get_text('')
                lst.append("""\n• """ + text[:98] + """...\n[Подробнее](""" + content + """)\n""")
                a = str(lst)
                b = re.sub(r"\['|\']|', '", '', a)
                c = re.sub(r"\\n", '\n', b)
                d = re.sub(r"- ", '\n- ', c)
            return """*Результаты поиска:* """ + """*'""" + self + """'*\n""" + d
        else:
            return """*Результаты поиска:* """ + """*'""" + self + """'*""" + """\nНичего не найдено"""
