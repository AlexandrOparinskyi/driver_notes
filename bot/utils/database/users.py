from sqlalchemy import select, insert

from database import User, get_async_session


async def get_user_by_id(user_id: int) -> User | None:
    """returning user by id"""
    async with get_async_session() as session:
        return await session.scalar(select(User).where(
            User.id == user_id
        ))


async def create_user(u_id: int,
                      username: str | None,
                      first_name: str,
                      last_name: str | None) -> None:
    """create new user"""
    async with get_async_session() as session:
        await session.execute(insert(User).values(
            id=u_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        ))
        await session.commit()
