import signal
import multitasking
from mailer import Mailer, EMAIL
from logger import no_recipient, mail_unsent
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

    mailer = Mailer()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = EMAIL

    for email, name in recipients:
        msg['To'] = email

        greet_name_template = env.get_template('greetname.txt')
        
        body = MIMEText(greet_name_template.render(contents=contents, name=name), 'plain')
        msg.attach(body)
        try:
            print 'Sending greeting email to %s' % email
            mailer.server.sendmail(msg.get('From'), email, msg.as_string())
        except Exception:
            mail_unsent(email)
            continue