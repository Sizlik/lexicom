from abc import ABC
from typing import List, TypeVar

from redis.asyncio import Redis

from src.repository.base_repository import BaseRepository


T = TypeVar("T")


class RedisRepository(BaseRepository[T], ABC):
    def __init__(self, redis: Redis, model_cls: str) -> None:
        self._redis = redis
        self._model_cls = model_cls

    async def get(self, **conditions) -> T:
        return await self._redis.get(f"{self._model_cls}:{conditions.get('name')}")

    async def add(self, record: T) -> T:
        return await self._redis.set(f"{self._model_cls}:{record.name}", record.value)

    async def update(self, record: T) -> T:
        if not await self.get(name=record.name):
            return False
        return await self.add(record)
