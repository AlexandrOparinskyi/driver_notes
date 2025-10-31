from fluentogram import TranslatorHub

from bot.utils import get_car_by_id
from database import GasStationTypeEnum, FuelTypeEnum


async def get_text_for_refuel_data(i18n: TranslatorHub,
                             data: dict) -> str:
    text = "\n"

    car = await get_car_by_id(int(data.get("refuel_car")))
    price = data.get("refuel_price")
    cur_price = float(price)
    date = data.get("refuel_date")
    curt_date = date.strftime("%d.%m.%Y")
    text += (f"<b>{i18n.refuel.record.car.button()}:</b> {car.name}\n"
             f"<b>{i18n.refuel.record.price.button()}:</b> {cur_price:.2f} ₽\n"
             f"<b>{i18n.refuel.record.date.button()}:</b> {curt_date}\n")

    liters = data.get("refuel_liters")
    if liters:
        text += (f"<b>{i18n.refuel.record.liters.button()}:</b> "
                 f"{liters}\n")

    refuel_station = data.get("refuel_station")
    if refuel_station:
        text += (f"<b>{i18n.refuel.record.station.button()}:</b> "
                 f"{GasStationTypeEnum[refuel_station].value}\n")

    refuel_type = data.get("refuel_type")
    if refuel_type:
        text += (f"<b>{i18n.refuel.record.fuel.type.button()}:</b> "
                 f"{FuelTypeEnum[refuel_type].value}\n")

    time = data.get("refuel_time")
    if time:
        text += (f"<b>{i18n.refuel.record.time.button()}:</b> "
                 f"{time}\n")

    return text


def get_text_for_edit_refuel_record_param(i18n: TranslatorHub,
                                          refuel_part: str) -> str:
    refuel_text_data = {
        "refuel_car": i18n.refuel.record.edit.car.text(),
        "refuel_price": i18n.refuel.record.edit.price.text(),
        "refuel_station": i18n.refuel.record.edit.station.text(),
        "refuel_type": i18n.refuel.record.edit.fuel.type.text(),
        "refuel_liters": i18n.refuel.record.edit.liters.text(),
        "refuel_time": i18n.refuel.record.edit.time.text(),
    }

    return refuel_text_data.get(refuel_part,
                                i18n.refuel.record.error.part.text())