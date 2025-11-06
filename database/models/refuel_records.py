import enum
from datetime import datetime

from sqlalchemy import ForeignKey, Enum, DateTime, func, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class FuelTypeEnum(enum.Enum):
    PETROL_92 = "92"
    PETROL_95 = "95"
    PETROL_98 = "98"
    PETROL_100 = "100"
    DIESEL = "Дизель"
    GAS = "Газ"
    ELECTRIC = "Электро"


class GasStationTypeEnum(enum.Enum):
    LUKOIL = "Лукойл"
    ROSNEFT = "Роснефть"
    GAZPROMNEFT = "Газпромнефть"
    TATNEFT = "Татнефть"
    SHELL = "Shell"
    BP = "BP"
    OTHER = "Другая"


class RefuelRecord(Base):
    __tablename__ = 'refuel_records'

    car_id: Mapped[int] = mapped_column(ForeignKey('cars.id',
                                                   ondelete="cascade"))

    total_price: Mapped[float] = mapped_column(Numeric(20, 2),
                                               nullable=False)
    liters: Mapped[float | None]
    fuel_type: Mapped[FuelTypeEnum | None] = mapped_column(
        Enum(FuelTypeEnum)
    )
    gas_station: Mapped[GasStationTypeEnum | None] = mapped_column(
        Enum(GasStationTypeEnum)
    )
    time: Mapped[float | None]
    full_tank: Mapped[bool | None]
    refuel_date: Mapped[datetime | None] = mapped_column(DateTime)

    car = relationship("Car",
                       back_populates="refuel_records",
                       lazy="joined")
