import smtplib

sender = 'ubushaev08@gmail.com'
receivers = ['ubushaev08@yandex.ru']

message = """From: From Person <ubushaev08@gmail.com>
To: To Person <ubushaev08@gmail.com>
Subject: Test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('mail.gmail.com', 25)
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")