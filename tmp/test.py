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
links = soup.find_all('a', 'search-result-link visitable', href=True)
desc = soup.find_all('div', 'highlights')
soup.prettify()

a = []
for line1 in desc:
    text = line1.get_text()
    #c.append(text)
    for line2 in links:
        url2 = SITE + line2['href']
    print(text + url2)

#print(a)

#print(str(a))

#print(content)

#a = re.findall(r'data(old)-totalsize', str(nores))
#print(a[0])
