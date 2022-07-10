from backend_queue import settings
from backend_queue.core import queues


def add_task(queue_name: str, task_name: str, *args, **kwargs):
    assert queue_name in queues.keys()

    queues[queue_name].enqueue_call(func=settings.tasks[queue_name][task_name],
                                    args=args, kwargs=kwargs)


def send_email(to: str, subject: str, text: str):
    add_task('email', 'send_email', to=to, subject=subject, text=text)
