from fluentogram import TranslatorHub

from bot.utils import get_user_by_id
from database import GasStationTypeEnum, FuelTypeEnum


def get_buttons_for_edit_refuel_record(i18n: TranslatorHub) -> list:
    return [
        (i18n.refuel.record.car.button(), "refuel_car"),
        (i18n.refuel.record.price.button(), "refuel_price"),
        (i18n.refuel.record.date.button(), "refuel_date"),
        (i18n.refuel.record.station.button(), "refuel_station"),
        (i18n.refuel.record.fuel.type.button(), "refuel_type"),
        (i18n.refuel.record.liters.button(), "refuel_liters"),
        (i18n.refuel.record.time.button(), "refuel_time"),
    ]


async def get_buttons_for_edit_refuel(i18n: TranslatorHub,
                                      refuel_part: str,
                                      user_id: int) -> list | None:
    user = await get_user_by_id(user_id)
    buttons = None

    if refuel_part == "refuel_car":
        buttons = [(c.name, c.id) for c in user.get_active_cars]

    if refuel_part == "refuel_station":
        buttons = [(s.value, s.name) for s in GasStationTypeEnum]

    if refuel_part == "refuel_type":
        buttons = [(t.value, t.name) for t in FuelTypeEnum]

    return buttons
