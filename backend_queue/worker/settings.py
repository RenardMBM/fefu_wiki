from os import getenv

QUEUE_NAMES = ["email"]
QUEUE_URL = ""

tasks = {
    'email': {
        'send_email': 'backend_queue.worker.tasks.send_email'
    }
}

# Email
EMAIL_DATA = {
    'email': getenv('SERVER_EMAIL'),
    'password': getenv('SERVER_EMAIL_PASSWORD'),
    'login': getenv('SERVER_EMAIL_LOGIN')
}
SMTP_SERVER = ('smtp.yandex.com', 465)
