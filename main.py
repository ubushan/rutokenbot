# -*- coding: utf-8 -*-
import re
import config
from urllib.request import urlopen
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


def parser(self):
    #print(self)
    self = self.encode('utf-8').decode('ascii', 'ignore')
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
        return """*Результаты поиска:* """ + """*'""" + self + """'\nНайдено: '""" + str(count3[0]) + """'*\n""" + d
    else:
        return """*Результаты поиска:* """ + """*'""" + self + """'*""" + """\nНичего не найдено"""


def mail(login, passwd, from_mail, to_mail, msg):
    mail_login = login
    mail_passwd = passwd
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587

    mail_from = from_mail
    mail_to = to_mail
    mail_subject = 'Сообщение от пользователя: ' + from_mail
    mail_text = msg + """\r

---
Письмо было отправленно посредством RutokenBot
"""

    message = MIMEText(mail_text)
    message['Subject'] = mail_subject
    message['From'] = from_mail
    message['To'] = mail_to
    message.set_charset('utf-8')
    print(message.as_string())

    mail = smtplib.SMTP(smtp_host, smtp_port)
    mail.ehlo()
    mail.starttls()
    mail.login(mail_login, mail_passwd)
    mail.sendmail(mail_from, mail_to, message.as_string())
    mail.close()