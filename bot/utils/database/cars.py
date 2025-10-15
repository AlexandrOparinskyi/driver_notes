from sqlalchemy import insert

from database import get_async_session, Car
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
