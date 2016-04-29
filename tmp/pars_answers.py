# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

SITE = 'http://kb.rutoken.ru'

def search_kb():
    url = 'http://www.rutoken.ru/support/feedback/#feedback'
    html_doc = urlopen(url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    text = (soup.find('div', 'base'))
    link = (soup.find_all('.dd', style='display: block;'))
    return (text.get_text() + '\n' + link.get_text())

print(search_kb())