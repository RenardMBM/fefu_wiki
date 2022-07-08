import smtplib
from email.message import EmailMessage

from backend_queue.worker import settings


def send_email(to: str, subject: str, text: str):
    msg = EmailMessage()
    msg.set_content(text)

    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_DATA['email']
    msg['To'] = to

    server = smtplib.SMTP_SSL(*settings.SMTP_SERVER)
    server.ehlo()
    # server.starttls()
    server.login(settings.EMAIL_DATA['login'], settings.EMAIL_DATA["password"])
    server.send_message(msg)
    server.quit()
