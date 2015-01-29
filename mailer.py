import smtplib
from email.mime.text import MIMEText
from config import *

class Mailer(object):

    def email(self, subject, text):
        msg = self.prepareMessage(subject, text)
        print(msg.as_string())
        self.sendMessage(msg)

    def prepareMessage(self, subject, text):
        msg = MIMEText(text)
        msg['From'] = SENDER
        msg['To'] = ', '.join(RECIPIENTS)
        msg['Subject'] = subject
        return msg

    def sendMessage(self, msg):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SENDER_LOGIN, SENDER_PASSWORD)
        server.sendmail(SENDER, RECIPIENTS, msg.as_string())
        server.quit()