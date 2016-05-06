# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

def mail(from_mail, msg):
    mail_login = ''
    mail_passwd = ''
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587

    mail_from = from_mail
    mail_to = ''
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

print('Введите Ваш электронный ящик')
from_mail = input()
print('Опишите свою проблему в общих чертах')
msg = input()

mail(from_mail, msg)