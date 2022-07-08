from backend_queue.core import queues


def add_task(queue_name: str, func: str, *args, **kwargs):
    assert queue_name in queues.keys()

    queues[queue_name].enqueue_call(func=func, args=args, kwargs=kwargs)
