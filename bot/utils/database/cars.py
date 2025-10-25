from sqlalchemy import insert, select, update

from database import get_async_session, Car, CarMark, CarModel, EngineTypeEnum, TransmissionTypeEnum
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


async def rename_car(car_id: int,
                     car_name: str) -> None:
    async with get_async_session() as session:
        await session.execute(update(Car).where(
            Car.id == car_id
        ).values(
            name=car_name
        ))
        await session.commit()


async def update_car_by_id(car_id: str,
                           user_id: int,
                           car_name: str | None,
                           car_mark: str | None = None,
                           car_model: str | None = None,
                           car_year: str | None = None,
                           car_color: str | None = None,
                           car_mileage: str | None = None,
                           car_engine: str | None = None,
                           car_transmission: str | None = None,
                           **kwargs) -> None:
    engine_type = EngineTypeEnum[car_engine] if car_engine else None
    transmission_type = (TransmissionTypeEnum[car_transmission]
                         if car_transmission else None)
    updated_values = {
        "user_id": user_id,
        "name": car_name,
        "mark": car_mark,
        "model": car_model,
        "year": int(car_year) if car_year else None,
        "color": car_color,
        "mileage": int(car_mileage) if car_mileage else None,
        "engine_type": engine_type,
        "transmission_type": transmission_type
    }

    async with get_async_session() as session:
        await session.execute(update(Car).where(
            Car.id == int(car_id)
        ).values(**updated_values))
        await session.commit()


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


async def get_car_mark_by_id(mark_id: int) -> CarMark:
    async with get_async_session() as session:
        return await session.scalar(select(CarMark).where(
            CarMark.id == mark_id
        ))


async def get_car_model_by_id(model_id: int) -> CarModel:
    async with get_async_session() as session:
        return await session.scalar(select(CarModel).where(
            CarModel.id == model_id
        ))
