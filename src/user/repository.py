from abc import ABC, abstractmethod
from typing import Optional

from redis.asyncio import Redis

from src.database import BaseRedisModel
from src.repository.base_repository import BaseRepository
from src.repository.redis_repository import RedisRepository
from src.user.schemas import UserBase


class UserRepositoryBase(BaseRepository[BaseRedisModel], ABC):
    @abstractmethod
    async def get_by_name(self, name: str) -> Optional[BaseRedisModel]:
        raise NotImplementedError()


class UserRepository(RedisRepository[BaseRedisModel], UserRepositoryBase):
    def __init__(self, redis: Redis) -> None:
        super().__init__(redis, "user")

    async def get_by_name(self, name: str) -> Optional[BaseRedisModel]:
        pass
