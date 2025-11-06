from sqlalchemy import insert

from database import get_async_session, ServicePart


async def create_service_parts(service_record_id: int,
                               data: dict[str, str]) -> None:
    quantity = data.get("part_quantity")
    price_per_unit = data.get("part_price_per_unit")
    total_price = data.get("part_price")

    updated_value = {
        "service_record_id": service_record_id,
        "name": data.get("part_name"),
        "part_number": data.get("part_number"),
        "quantity": float(quantity) if quantity else None,
        "price_per_unit": float(price_per_unit) if price_per_unit else None,
        "total_price": float(total_price) if total_price else 0,
        "comment": data.get("part_comment")
    }
    async with get_async_session() as session:
        await session.execute(insert(ServicePart).values(
            **updated_value
        ))
        await session.commit()
