from os import getenv

QUEUE_NAMES = ["email"]
QUEUE_URL = ""

tasks = {
    'email': {
        'send_message': 'backend_queue.worker.tasks.send_email'
    }
}

# Email
EMAIL_DATA = {  # TODO: создать аккаунт и протестировать
    'email': getenv('SERVER_EMAIL'),
    'password': getenv('SERVER_EMAIL_PASSWORD')
}
SMTP_SERVER = ('smpt.gmail.com', 587)
