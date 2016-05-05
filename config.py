# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


TOKEN = '186044924:AAHUcAUHTg-gjgZMylRgmD4tUYl2t94AzcQ'
SITE = 'http://kb.rutoken.ru'


class head():
    def float_check(self):
        try:
            float(self)
            return True
        except ValueError:
            return False


    def search_kb(self):
        url = SITE + "/dosearchsite.action?cql=siteSearch+~+" + '"' + self + '"' + "+and+space+%3D+" + "KB" + "+and+type+%3D+" + "page" + "&queryString=" + self
        html_doc = urlopen(url).read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        check = soup.find_all('div', 'search-results-container')
        count = soup.find_all('p', 'search-results-count')
        count2 = re.findall(r'\Showing \d* ', str(count))
        count3 = re.findall(r' \d* ', str(count2))
        #print(count3[0])
        result = re.findall(r'data(old)-totalsize', str(check))
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
