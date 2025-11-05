from datetime import date

from sqlalchemy import insert, update

from database import get_async_session, CarDocument


async def create_car_documents(car_id: int) -> None:
    async with get_async_session() as session:
        await session.execute(insert(CarDocument).values(
            car_id=car_id
        ))
        await session.commit()


async def update_car_documents(car_id: int,
                               car_doc: str,
                               doc_value: str | date) -> None:
    async with get_async_session() as session:
        await session.execute(update(CarDocument).where(
            CarDocument.car_id == car_id
        ).values(
            **{car_doc: doc_value}
        ))
        await session.commit()
