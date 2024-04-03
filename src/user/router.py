from fastapi import APIRouter, Query, Depends

from src.database import BaseRedisModel
from src.repository.dependencies import get_unit_of_work
from src.repository.uow import UnitOfWork
from src.user.schemas import UserCreate, UserUpdate

router = APIRouter(tags=["user"])


@router.get("/check_data")
async def check_user_data(phone=Query(str), uow: UnitOfWork = Depends(get_unit_of_work)):
    return await uow.users.get(name=phone)


@router.post("/write_data")
async def create_user_data(user: UserCreate, uow: UnitOfWork = Depends(get_unit_of_work)):
    brm = BaseRedisModel(name=user.phone, value=user.address)
    return await uow.users.add(brm)


@router.put("/write_data")
async def update_user_data(user: UserUpdate, uow: UnitOfWork = Depends(get_unit_of_work)):
    brm = BaseRedisModel(name=user.phone, value=user.address)
    response = await uow.users.update(brm)

    if not response:
        return {"message": "Данные не найдены"}

    return response
