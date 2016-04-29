# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

SITE = 'http://kb.rutoken.ru'

self = input()
url = SITE + "/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "&queryString=" + self
html_doc = urlopen(url).read()
soup = BeautifulSoup(html_doc, 'html.parser')
nores = soup.find_all('div', 'search-results-container')

print(nores)

a = re.findall(r'data-totalsize', str(nores))
print(a[0])
