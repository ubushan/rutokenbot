# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

SITE = 'http://kb.rutoken.ru'

def search_kb(self):
    url = SITE + "/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "&queryString=" + self
    html_doc = urlopen(url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # text = (soup.find_all('div', 'highlights'))
    for link in soup.find_all('a', 'search-result-link visitable'):
        a = print(link.get('href'))
    return a

search_kb('10')