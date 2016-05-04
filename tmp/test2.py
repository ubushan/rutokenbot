# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

SITE = 'http://kb.rutoken.ru'

def noresults(self):
    url = SITE + "/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "&queryString=" + self
    html_doc = urlopen(url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    nores = soup.find_all('div', 'search-results-container')
    a = re.findall(r'No results', str(nores))
    return a[0]

print(noresults(200))