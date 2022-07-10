from os import getenv

REDIS_URL = f"redis://{getenv('REDIS_HOST', 'localhost')}:{getenv('REDIS_PORT', '6379')}"

tasks = {
    'email': {
        'send_email': 'tasks.send_email'
    }
}
