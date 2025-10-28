from fluentogram import TranslatorHub

from bot.utils import get_car_by_id
from database import ServiceTypeEnum


async def get_text_for_service_data(i18n: TranslatorHub,
                                    data: dict) -> str:

    text = "\n"

    title = data.get("service_title")
    if title:
        text += f"<b>{i18n.service.title.button()}:</b> {title}\n"

    car_id = data.get("service_car")
    if car_id:
        car = await get_car_by_id(int(car_id))
        if car.name:
            text += f"<b>{i18n.service.car.button()}:</b> {car.name}\n"
        mileage = data.get("service_mileage")
        if mileage:
            text += f"<b>{i18n.service.mileage.button()}:</b> {mileage}\n"
        elif car.mileage:
            text += f"<b>{i18n.service.mileage.button()}:</b> {car.mileage}\n"

    description = data.get("service_description")
    if description:
        text += f"<b>{i18n.service.description.button()}:</b> {description}\n"

    date = data.get("service_date")
    if date:
        text += (f"<b>{i18n.service.date.button()}:</b> "
                 f"{date.strftime('%d.%m.%Y')}\n")

    s_type = data.get("service_type")
    if s_type:
        text += (f"<b>{i18n.service.type.button()}:</b> "
                 f"{ServiceTypeEnum[s_type].value}\n")

    price = data.get("service_price")
    if price:
        text += f"<b>{i18n.service.price.button()}:</b> {price}\n"

    name = data.get("service_name")
    if name:
        text += f"<b>{i18n.service.name.button()}:</b> {name}\n"

    return text


def get_text_for_edit_service_record_part(i18n: TranslatorHub,
                                          service_part: str) -> str:
    text_data = {
        "service_title": i18n.service.record.edit.title.text(),
        "service_description": i18n.service.record.edit.description.text(),
        "service_name": i18n.service.record.edit.name.text(),
        "service_price": i18n.service.record.edit.price.text(),
        "service_mileage": i18n.service.record.edit.mileage.text()
    }

    return text_data.get(service_part, i18n.service.record.error.part.text())
