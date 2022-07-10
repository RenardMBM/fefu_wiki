import redis
from rq import Worker, Connection

from settings import REDIS_URL

if __name__ == '__main__':
    conn = redis.from_url(REDIS_URL)
    with Connection(conn):
        worker = Worker(["email"])
        worker.work()
