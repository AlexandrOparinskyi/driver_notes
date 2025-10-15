import enum
from datetime import datetime

from sqlalchemy import DateTime, func, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class EngineTypeEnum(enum.Enum):
    PETROL = "Бензин"
    DIESEL = "Дизель"
    ELECTRO = "Электро"
    HYBRID = "Гибрид"
    GAS = "Газ"


class TransmissionTypeEnum(enum.Enum):
    AUTOMATIC = "Автоматическая"
    MANUAL = "Механическая"
    CVT = "Вариатор"
    ROBOTIC = "Робот"


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    mark: Mapped[str | None]
    model: Mapped[str | None]
    year: Mapped[int | None]
    color: Mapped[str | None]
    engine_type: Mapped[EngineTypeEnum | None] = mapped_column(
        Enum(EngineTypeEnum)
    )
    transmission_type: Mapped[TransmissionTypeEnum | None] = mapped_column(
        Enum(TransmissionTypeEnum)
    )
    mileage: Mapped[int | None]
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 server_default=func.now(),
                                                 nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id',
                                                    ondelete='CASCADE'),
                                         nullable=False)
    is_deleted: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_selected_main: Mapped[bool] = mapped_column(default=False,
                                                   nullable=False)

    user = relationship("User",
                        back_populates="cars",
                        lazy="joined")
