import random
import uuid

from sqlalchemy import String, Integer, create_engine, UUID
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


engine = create_engine("postgresql+psycopg2://user:user@localhost:5431/main", echo=True)

FullNames.__table__.drop(engine)
ShortNames.__table__.drop(engine)

Base.metadata.create_all(engine)

with Session(engine) as session:
    for i in range(700000):
        sn = ShortNames(
            name=f"file{i}",
            status=random.randint(0, 2)
        )
        session.add(sn)
    for i in range(500000):
        fn = FullNames(
            name=f"file{i}.mp3"
        )
        session.add(fn)
    session.commit()

