from abc import abstractmethod, ABC
from typing import Callable

from redis.asyncio import Redis

from src.user.repository import UserRepositoryBase, UserRepository


class UnitOfWorkBase(ABC):
    users: UserRepositoryBase

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.rollback()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError()

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()


class UnitOfWork(UnitOfWorkBase):
    def __init__(self, redis: Redis) -> None:
        self._redis = redis

    async def __aenter__(self):
        self.users = UserRepository(self._redis)
        return await super().__aenter__()

    async def commit(self):
        pass

    async def rollback(self):
        pass
