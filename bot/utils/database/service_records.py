from sqlalchemy import insert, select, delete

from database import get_async_session, ServiceTypeEnum, ServiceRecord


async def create_service_record(user_id: int,
                                service_car: str | None = None,
                                service_title: str | None = None,
                                service_name: str | None = None,
                                service_description: str | None = None,
                                service_date: str | None = None,
                                service_type: str | None = None,
                                service_price: str | None = None,
                                **kwargs) -> int | None:
    s_type = ServiceTypeEnum[service_type] if service_type else None

    if service_price is None:
        service_price = 0
        if kwargs.get("part_data"):
            service_price += sum(float(
                i.get("part_price", 0)
            ) for i in kwargs.get("part_data").values())
        if kwargs.get("work_data"):
            service_price += sum(float(
                i.get("work_price", 0)
            ) for i in kwargs.get("work_data").values())

    created_values = {
        "user_id": int(user_id),
        "car_id": int(service_car) if service_car else None,
        "title": service_title,
        "description": service_description,
        "service_date": service_date,
        "service_center": service_name,
        "total_price": float(service_price) if service_price else 0,
        "service_type": s_type
    }

    async with get_async_session() as session:
        query = await session.execute(insert(ServiceRecord).values(
            **created_values
        ).returning(ServiceRecord.id))
        await session.commit()

        result = query.scalar_one_or_none()
        return result


async def get_service_by_id(service_id: int) -> ServiceRecord:
    async with get_async_session() as session:
        return await session.scalar(select(ServiceRecord).where(
            ServiceRecord.id == service_id
        ))


async def delete_service_by_id(service_id: int) -> None:
    async with get_async_session() as session:
        await session.execute(delete(ServiceRecord).where(
            ServiceRecord.id == service_id
        ))
        await session.commit()
