from sqlalchemy import insert

from database import get_async_session, ServiceWork


async def create_service_works(service_record_id: int,
                               data: dict[str, str]) -> None:
    price = data.get("work_price")

    updated_value = {
        "service_record_id": service_record_id,
        "name": data.get("work_name"),
        "description": data.get("work_description"),
        "price": float(price) if price else 0,
    }
    async with get_async_session() as session:
        await session.execute(insert(ServiceWork).values(
            **updated_value
        ))
        await session.commit()
