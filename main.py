# -*- coding: utf-8 -*-
import re
import config
from urllib.request import urlopen
from bs4 import BeautifulSoup


def parser(self):
    #print(self)
    #self = self.encode('utf-8').decode('ascii', 'ignore')
    url = config.KB + "/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "+and+type+%3D+" + "page" + "&queryString=" + self
    html_doc = urlopen(url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    check = soup.find_all('div', 'search-results-container')
    count = soup.find_all('p', 'search-results-count')
    count2 = re.findall(r'\Showing \d* ', str(count))
    count3 = re.findall(r' \d* ', str(count2))
    result = re.findall(r'data-totalsize', str(check))
    if bool(result) == True:
        lst = []
        for link in soup.find_all('a', 'search-result-link visitable'):
            content = config.KB + link.get('href')
        for descript in soup.find_all('div', 'highlights'):
            text = descript.get_text('')
            lst.append("""\n• """ + text[:98] + """...\n[Подробнее](""" + content + """)\n""")
            a = str(lst)
            b = re.sub(r"\['|\']|', '", '', a)
            c = re.sub(r"\\n", '\n', b)
            d = re.sub(r"- ", '\n- ', c)
        return """*Результаты поиска:* """ + """*'""" + self + """'\nНайдено:'""" + str(count3[0]) + """'*\n""" + d
    else:
        return """*Результаты поиска:* """ + """*'""" + self + """'*""" + """\nНичего не найдено"""