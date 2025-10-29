import enum
from datetime import datetime

from sqlalchemy import ForeignKey, Text, DateTime, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class ServiceTypeEnum(enum.Enum):
    REPLACEMENT = "Замена"
    MAINTENANCE = "ТО"
    DIAGNOSTICS = "Диагностика"
    REPAIR = "Ремонт"
    BODY_WORK = "Кузовные работы"
    OTHER = "Другое"

    def get_smile(self) -> str:
        smiles = {
            ServiceTypeEnum.REPLACEMENT: "🛠️",
            ServiceTypeEnum.MAINTENANCE: "🔧",
            ServiceTypeEnum.DIAGNOSTICS: "📊",
            ServiceTypeEnum.REPAIR: "🔩",
            ServiceTypeEnum.BODY_WORK: "🎨",
            ServiceTypeEnum.OTHER: "❓"
        }
        return smiles.get(self, "⚙️")


class ServiceRecord(Base):
    __tablename__ = "service_records"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id",
                   ondelete="cascade"),
        nullable=False
    )
    car_id: Mapped[int | None] = mapped_column(
        ForeignKey("cars.id",
                   ondelete="cascade")
    )

    title: Mapped[str | None]
    description: Mapped[str | None] = mapped_column(Text)
    total_price: Mapped[float] = mapped_column(Numeric(20, 2),
                                               nullable=False,
                                               default=0)
    service_type: Mapped[ServiceTypeEnum | None] = mapped_column(
        Enum(ServiceTypeEnum)
    )
    service_center: Mapped[str | None]
    service_date: Mapped[datetime | None] = mapped_column(DateTime)

    user = relationship("User",
                        back_populates="service_records")
    car = relationship("Car",
                       back_populates="service_records")
    service_works = relationship("ServiceWork",
                                 back_populates="service_record",
                                 lazy="selectin")
    service_parts = relationship("ServicePart",
                                 back_populates="service_record",
                                 lazy="selectin")


class ServiceWork(Base):
    __tablename__ = "service_works"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_record_id: Mapped[int] = mapped_column(
        ForeignKey("service_records.id",
                   ondelete="cascade"),
        nullable=False
    )

    name: Mapped[str | None]
    description: Mapped[str | None]
    price: Mapped[float] = mapped_column(Numeric(20, 2))

    service_record = relationship("ServiceRecord",
                                  back_populates="service_works")


class ServicePart(Base):
    __tablename__ = "service_parts"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_record_id: Mapped[int] = mapped_column(
        ForeignKey("service_records.id",
                   ondelete="cascade"),
        nullable=False
    )

    name: Mapped[str | None]
    part_number: Mapped[str | None]
    quantity: Mapped[float | None]
    price_per_unit: Mapped[float | None] = mapped_column(Numeric(20, 2))
    total_price: Mapped[float | None] = mapped_column(Numeric(20, 2))
    comment: Mapped[str | None]

    service_record = relationship("ServiceRecord",
                                  back_populates="service_parts")
