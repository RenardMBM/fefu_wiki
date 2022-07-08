from backend_queue.worker.services import create_workers
from backend_queue.worker import settings

if __name__ == '__main__':
    worker_queues = {}
    for key, value in settings.tasks.items():
        worker_queues[key] = len(value)
    create_workers(worker_queues)
