from sqlalchemy import insert, select

from database import get_async_session, Car, CarMark, CarModel
from .users import get_user_by_id


async def create_car(car_name: str,
                     user_id: int) -> int:
    """create new car and returning her id"""
    user = await get_user_by_id(user_id)
    flag = False
    if user.get_main_car is None:
        flag = True

    async with get_async_session() as session:
        query = await session.execute(insert(Car).values(
            name=car_name,
            user_id=user_id,
            is_selected_main=flag
        ).returning(Car.id))
        await session.commit()
        car_id = query.scalar_one_or_none()

        return car_id


async def get_car_by_id(car_id: int) -> Car | None:
    async with get_async_session() as session:
        return await session.scalar(select(Car).where(
            Car.id == car_id
        ))


async def edit_car_by_id(car_id: int,
                         car_name: str | None):
    pass


async def get_car_marks() -> list[CarMark]:
    async with get_async_session() as session:
        return await session.scalars(select(CarMark).order_by(
            CarMark.rating
        ))


async def get_car_models(mark_id: str | None) -> list[CarModel]:
    async with get_async_session() as session:
        if mark_id:
            return await session.scalars(select(CarModel).where(
                CarModel.mark_id == int(mark_id)
            ).order_by(CarModel.rating))

        return await session.scalars(select(CarModel).order_by(
            CarModel.rating
        ).limit(21))

