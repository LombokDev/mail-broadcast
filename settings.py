import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIL_LOGGER_PATH = os.path.abspath('app/mailing/logs/mailing.log')
MAIL_TLS_PORT = 587
MAIL_SERVER = 'smtp.gmail.com:%d' % MAIL_TLS_PORT

#GMAIL CREDENTIALS
EMAIL = os.environ.get('LOMBOK_DEV_EMAIL')
PASS = os.environ.get('LOMBOK_DEV_EMAIL_PASS')

