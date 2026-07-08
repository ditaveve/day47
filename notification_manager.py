import os
from dotenv import load_dotenv
import json
import smtplib

class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.MY_EMAIL = os.getenv('MY_EMAIL')
        self.MY_EMAIL_PASSWORD = os.getenv('MY_EMAIL_PASSWORD')
        self.RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL', self.MY_EMAIL)

    def send_emails(self, message):
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        connection.login(user=self.MY_EMAIL, password=self.MY_EMAIL_PASSWORD)
        connection.sendmail(from_addr=self.MY_EMAIL, to_addrs=self.RECEIVER_EMAIL, msg=message.encode('utf-8'))