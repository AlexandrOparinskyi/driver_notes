from aiogram.types import User
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id


async def getter_garage(i18n: TranslatorHub,
                        event_from_user: User,
                        **kwargs) -> dict[str, str | list]:
    user = await get_user_by_id(event_from_user.id)

    return {"garage_text": i18n.garage.text(username=user.first_name),
            "home_button": i18n.home.button(),
            "add_car_button": i18n.add.car.button(),
            "cars": user.get_active_cars}


async def getter_car_name(i18n: TranslatorHub,
                          **kwargs) -> dict[str, str]:
    return {"car_name_text": i18n.car.name.text(),
            "back_button": i18n.back.button()}
