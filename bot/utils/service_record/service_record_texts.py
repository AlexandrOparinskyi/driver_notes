from fluentogram import TranslatorHub

from bot.utils import get_user_by_id, get_car_by_id
from database import ServiceTypeEnum


async def get_text_for_service_data(i18n: TranslatorHub,
                                    user_id: int,
                                    data: dict) -> str:
    user = await get_user_by_id(user_id)
    main_car = user.get_main_car
    mileage = main_car.mileage
    text = "\n"

    car_id = data.get("service_car")
    if car_id:
        main_car = await get_car_by_id(car_id)
        if main_car.mileage:
            mileage = main_car.mileage

    new_mileage = data.get("service_mileage")

    if main_car is not None:
        text += f"<b>{i18n.service.car.button()}:</b> {main_car.name}\n"

    if not new_mileage:
        text += (f"<b>{i18n.service.mileage.button()}:</b> "
                 f"{mileage if mileage else i18n.field.no.filled()}\n")
    else:
        text += (f"<b>{i18n.service.mileage.button()}:</b> "
                 f"{new_mileage}\n")

    title = data.get("service_title")
    if title:
        text += f"<b>{i18n.service.title.button()}:</b> {title}\n"

    description = data.get("service_description")
    if description:
        text += f"<b>{i18n.service.description.button()}:</b> {description}\n"

    date = data.get("service_date")
    if description:
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
