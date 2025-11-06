from sqlalchemy import insert, select, delete, update

from database import get_async_session, RefuelRecord, FuelTypeEnum, GasStationTypeEnum


async def create_refuel_record(refuel_car: str,
                               refuel_price: str,
                               refuel_date: str | None = None,
                               refuel_station: str | None = None,
                               refuel_type: str | None = None,
                               refuel_liters: str | None = None,
                               refuel_time: str | None = None,
                               full_tank: bool | None = None,
                               **kwargs) -> None:
    gas_station = (GasStationTypeEnum[refuel_station]
                   if refuel_station else None)
    fuel_type = FuelTypeEnum[refuel_type] if refuel_type else None

    created_value = {
        "car_id": int(refuel_car),
        "total_price": float(refuel_price),
        "liters": float(refuel_liters) if refuel_liters else None,
        "fuel_type": fuel_type,
        "gas_station": gas_station,
        "time": refuel_time,
        "full_tank": full_tank if full_tank else False,
        "refuel_date": refuel_date
    }

    async with get_async_session() as session:
        await session.execute(insert(RefuelRecord).values(
            **created_value
        ))
        await session.commit()


async def get_refuel_by_id(refuel_id: int) -> RefuelRecord:
    async with get_async_session() as session:
        return await session.scalar(select(RefuelRecord).where(
            RefuelRecord.id == refuel_id
        ))


async def delete_refuel_by_id(refuel_id: int) -> None:
    async with get_async_session() as session:
        await session.execute(delete(RefuelRecord).where(
            RefuelRecord.id == refuel_id
        ))
        await session.commit()


async def update_refuel_record(record_id: str,
                               refuel_car: str,
                               refuel_price: str,
                               refuel_date: str | None = None,
                               refuel_station: str | None = None,
                               refuel_type: str | None = None,
                               refuel_liters: str | None = None,
                               refuel_time: str | None = None,
                               full_tank: bool | None = None,
                               **kwargs) -> None:
    gas_station = (GasStationTypeEnum[refuel_station]
                   if refuel_station else None)
    fuel_type = FuelTypeEnum[refuel_type] if refuel_type else None

    updated_value = {
        "car_id": int(refuel_car),
        "total_price": float(refuel_price),
        "liters": float(refuel_liters) if refuel_liters else None,
        "fuel_type": fuel_type,
        "gas_station": gas_station,
        "time": refuel_time,
        "full_tank": full_tank if full_tank else False,
        "refuel_date": refuel_date
    }

    async with get_async_session() as session:
        await session.execute(update(RefuelRecord).where(
            RefuelRecord.id == int(record_id)
        ).values(
            **updated_value
        ))
        await session.commit()
