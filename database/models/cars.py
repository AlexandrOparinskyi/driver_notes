import enum
from datetime import datetime

from sqlalchemy import DateTime, func, ForeignKey, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class EngineTypeEnum(enum.Enum):
    PETROL = "Бензин"
    DIESEL = "Дизель"
    ELECTRO = "Электро"
    HYBRID = "Гибрид"
    GAS = "Газ"


class TransmissionTypeEnum(enum.Enum):
    AUTOMATIC = "Автомат"
    MANUAL = "Механика"
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
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id',
                                                    ondelete='CASCADE'),
                                         nullable=False)
    is_deleted: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_selected_main: Mapped[bool] = mapped_column(default=False,
                                                   nullable=False)

    user = relationship("User",
                        back_populates="cars")
    service_records = relationship("ServiceRecord",
                                   back_populates="car",
                                   lazy="selectin")
    refuel_records = relationship("RefuelRecord",
                                  back_populates="car",
                                  lazy="selectin")

    @property
    def to_dict(self) -> dict:
        transmission = (self.transmission_type.name if
                        self.transmission_type else None)
        engine = self.engine_type.name if self.engine_type else None

        return {"car_id": self.id,
                "car_name": self.name,
                "car_mark": self.mark,
                "car_model": self.model,
                "car_year": self.year,
                "car_color": self.color,
                "car_engine": engine,
                "car_transmission": transmission}

    @property
    def get_total_price(self) -> str:
        return str(sum([s.total_price if s.total_price else 0
                        for s in self.service_records]) +
                   sum([r.total_price if r.total_price else 0
                        for r in self.refuel_records]))

    @property
    def get_recent_activities(self) -> list:
        return list(sorted(self.service_records + self.refuel_records,
                           key=lambda x: x.created_at,
                           reverse=True))


class CarMark(Base):
    __tablename__ = "car_marks"

    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    rating: Mapped[int] = mapped_column(default=0, nullable=False)


class CarModel(Base):
    __tablename__ = "car_models"
    __table_args__ = (
        UniqueConstraint("name", "mark_id", name="unique_mark_model"),
    )

    name: Mapped[str] = mapped_column(nullable=False)
    mark_id: Mapped[int] = mapped_column(ForeignKey("car_marks.id",
                                                    ondelete="CASCADE"),
                                         nullable=False)
    rating: Mapped[int] = mapped_column(default=0, nullable=False)

    mark = relationship("CarMark", lazy="joined")
