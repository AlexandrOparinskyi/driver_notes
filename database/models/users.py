from sqlalchemy import BigInteger, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, LocaleTypeEnum
from .cars import Car


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str | None] = mapped_column(unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str | None]

    is_premium: Mapped[bool] = mapped_column(default=False, nullable=False)
    bonus_points: Mapped[int] = mapped_column(default=0, nullable=False)
    is_banned: Mapped[bool] = mapped_column(default=False, nullable=False)

    locale: Mapped[LocaleTypeEnum] = mapped_column(Enum(LocaleTypeEnum),
                                                   default=LocaleTypeEnum.RU)

    cars = relationship("Car",
                        back_populates="user",
                        lazy="selectin")
    service_records = relationship("ServiceRecord",
                                   back_populates="user",
                                   lazy="selectin")
    payments = relationship("Payment",
                            back_populates="user",
                            lazy="selectin")

    @property
    def get_active_cars(self) -> list[Car]:
        return [c for c in self.cars if c.is_active and not c.is_deleted]

    @property
    def get_main_car(self) -> Car | None:
        try:
            return [c for c in self.cars
                    if c.is_selected_main and not c.is_deleted][0]
        except IndexError:
            return None

    @property
    def get_records(self):
        records = []
        for car in self.get_active_cars:
            records += car.get_records()
        return records
