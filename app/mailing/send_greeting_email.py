import signal
import multitasking
from .mailer import Mailer, EMAIL
from logger import no_recipient, mail_unsent, log
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from startup import env

# ctr+c to kill
signal.signal(signal.SIGINT, multitasking.killall)

# we use no shared resourcesuse, so use "process" instead of thread.
multitasking.set_engine("process")


@multitasking.task
def send_greeting_email(subject, contents, recipients=list()):
    if recipients.__len__() <= 0:
        no_recipient()
        return

    #instance one smtp for given email credentials
    mailer = Mailer()
    for email, name in recipients:
        # 1 email msg for 1 recipient
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = EMAIL
        msg['To'] = email

        greet_name_template = env.get_template('greetname.txt')

        body = MIMEText(
            greet_name_template.render(contents=contents, name=name.title()),
            'plain')
        msg.attach(body)
        try:
            print 'Sending greeting email to %s' % email
            log.info('Sending greeting email to %s' % email)
            mailer.server.sendmail(msg.get('From'), email, msg.as_string())
        except Exception:
            mail_unsent(email)
            continue