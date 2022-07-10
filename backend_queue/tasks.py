from os import getenv
import smtplib
from email.message import EmailMessage


EMAIL_DATA = {
    'email': getenv('SERVER_EMAIL'),
    'password': getenv('SERVER_EMAIL_PASSWORD'),
    'login': getenv('SERVER_EMAIL_LOGIN')
}

SMTP_SERVER = ('smtp.yandex.com', 465)


def send_email(to: str, subject: str, text: str):
    msg = EmailMessage()
    msg.set_content(text)

    msg['Subject'] = subject
    msg['From'] = EMAIL_DATA['email']
    msg['To'] = to

    server = smtplib.SMTP_SSL(*SMTP_SERVER)
    server.ehlo()
    # server.starttls()
    server.login(EMAIL_DATA['login'], EMAIL_DATA["password"])
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    send_email('baderik.pm@students.dvfu.ru', 'Мы прислушались к вам', 'Test message')
