from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")


class BaseRepository(Generic[T], ABC):
    @abstractmethod
    async def get(self, **conditions) -> T:
        raise NotImplementedError()

    @abstractmethod
    async def add(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, record: T) -> T:
        raise NotImplementedError()



