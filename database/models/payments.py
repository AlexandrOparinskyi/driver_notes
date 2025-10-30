import enum

from sqlalchemy import Enum, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class PaymentTypeEnum(enum.Enum):
    DONATE = "DONATE"
    SUBSCRIBE = "SUBSCRIBE"


class Payment(Base):
    __tablename__ = 'payments'

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id",
                                                    ondelete="SET NULL"))
    payment_id: Mapped[str]
    payment_type: Mapped[PaymentTypeEnum] = mapped_column(
        Enum(PaymentTypeEnum)
    )
    status: Mapped[str] = mapped_column(String(50))
    amount: Mapped[float]

    user = relationship("User", back_populates="payments")
