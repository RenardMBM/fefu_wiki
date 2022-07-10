import redis
from rq import Queue

from backend_queue.settings import REDIS_URL

conn = redis.from_url(REDIS_URL)

queues = {"email": Queue("email", connection=conn)}
