from aiogram.types import User
from fluentogram import TranslatorHub


async def getter_garage(i18n: TranslatorHub,
                        event_from_user: User,
                        **kwargs) -> dict[str, str]:
    username = event_from_user.first_name

    return {"garage_text": i18n.garage.text(username=username),
            "home_button": i18n.home.button(),
            "add_car_button": i18n.add.car.button()}
