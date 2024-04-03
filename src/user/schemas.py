from pydantic import BaseModel


class UserBase(BaseModel):
    phone: str
    address: str


class UserRead(UserBase):
    pass


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
