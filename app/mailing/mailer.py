import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
from settings import EMAIL, PASS, MAIL_SERVER, MAIL_TLS_PORT

class Mailer:
    def __init__(self, *args, **kwargs):
      socket.setdefaulttimeout(60 * 5)
      self.connect_and_login()

    def connect_and_login(self):
      self.connect()
      self.login()

    def connect(self):
      self.server = smtplib.SMTP(MAIL_SERVER)

    def login(self):
      self.server.starttls()
      self.server.login(EMAIL, PASS)
