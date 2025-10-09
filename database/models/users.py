from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str | None] = mapped_column(unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str | None]

    is_premium: Mapped[bool] = mapped_column(default=False, nullable=False)
    bonus_points: Mapped[int] = mapped_column(default=0, nullable=False)
    is_banned: Mapped[bool] = mapped_column(default=False, nullable=False)
