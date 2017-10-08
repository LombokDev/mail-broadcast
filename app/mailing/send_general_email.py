from mailer import Mailer, EMAIL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logger import no_recipient
from startup import env
from logger import log


def send_general_email(subject, contents, recipients=list()):
    if recipients.__len__() <= 0:
        no_recipient()
        return
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = EMAIL

    general = env.get_template('base.txt')

    body = MIMEText(general.render(contents=contents), 'plain')
    msg.attach(body)

    mailer = Mailer()
    try:
        log.info('Sending general email')
        mailer.server.sendmail(msg.get('From'), recipients, msg.as_string())
    except Exception as e:
        log.error('An error occured %s' % e.message)

