from rq import Worker, Connection

from backend_queue.core import queues, conn
from backend_queue.worker import settings
from backend_queue.services import add_task


def create_workers(for_queues: dict[str, int]):
    assert all(map(lambda queue_name: queue_name in queues, for_queues))

    workers_queues = []
    for key, value in for_queues.items():
        for i in range(value):
            workers_queues.append(queues[key])
    with Connection(conn):
        worker = Worker(workers_queues)
        worker.work(with_scheduler=True)


def create_task(queue_name: str, task_name: str, *args, **kwargs):
    add_task(queue_name, settings.tasks[queue_name][task_name], *args, **kwargs)


def send_email(to: str, subject: str, text: str):
    add_task('email', settings.tasks['email']['send_email'], to=to, subject=subject, text=text)
