import random
import uuid

from sqlalchemy import String, Integer, create_engine, UUID, select
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session


class Base(DeclarativeBase):
    pass


class ShortNames(Base):
    __tablename__ = "short_names"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(30))
    status: Mapped[int] = mapped_column(Integer, nullable=True)


class FullNames(Base):
    __tablename__ = "full_names"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(30))
    status: Mapped[int] = mapped_column(Integer, nullable=True)


engine = create_engine("postgresql+psycopg2://user:user@localhost:5431/main")


with Session(engine) as session:
    for i in session.scalars(select(ShortNames)).all():
        print(i.name)
        obj = session.scalar(select(FullNames).where(FullNames.name == i.name + ".mp3"))
        if obj:
            print(i.name, i.status == obj.status)
            if i.status != obj.status:
                print("ОШИБКА!", obj.name, obj.status, i.name, i.status)
                break
        else:
            print(i.name, "не найден")
            break
