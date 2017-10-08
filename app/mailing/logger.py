import logging
from settings import MAIL_LOGGER_PATH

log = logging.getLogger('mailingbroadcast')
handler = logging.FileHandler(MAIL_LOGGER_PATH)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.INFO)


def mail_unsent(email):
    log.error('Gagal mengirim email ke %s ' % email)

def no_recipient():
    log.error('Email tidak dikirim, penerima tidak ditentukan')