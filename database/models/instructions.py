from sqlalchemy import String, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, LocaleTypeEnum


class Instruction(Base):
    __tablename__ = "instructions"

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    locale: Mapped[LocaleTypeEnum] = mapped_column(Enum(LocaleTypeEnum),
                                                   nullable=False)
    text: Mapped[str] = mapped_column(Text)
