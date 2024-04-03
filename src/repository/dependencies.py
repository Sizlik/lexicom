from src.database import redis
from src.repository.uow import UnitOfWork, UnitOfWorkBase


async def get_unit_of_work() -> UnitOfWorkBase:
    async with UnitOfWork(redis) as uow:
        yield uow
