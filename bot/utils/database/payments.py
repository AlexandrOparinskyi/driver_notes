from sqlalchemy import select, insert

from database import Payment, get_async_session, PaymentTypeEnum


async def get_payment_by_id(payment_id: str,
                            user_id: int) -> Payment | None:
    async with get_async_session() as session:
        return await session.scalar(select(Payment).where(
            Payment.payment_id == payment_id,
            Payment.user_id == user_id,
        ))


async def create_payment_db(user_id: int,
                            payment_id: str,
                            amount: float,
                            status: str,
                            payment_type: str):
    async with get_async_session() as session:
        await session.execute(insert(Payment).values(
            user_id=user_id,
            payment_id=payment_id,
            amount=amount,
            status=status,
            payment_type=PaymentTypeEnum[payment_type.upper()]
        ))
        await session.commit()
