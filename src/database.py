import os

import redis.asyncio
from pydantic import BaseModel

redis_url = os.getenv("REDIS_URL", "redis://redis:6379")

redis = redis.asyncio.from_url(redis_url)


class BaseRedisModel(BaseModel):
    name: str
    value: str
