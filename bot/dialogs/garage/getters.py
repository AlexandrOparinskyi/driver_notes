from aiogram.types import User
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id
from config import PREMIUM_PRICE


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


async def getter_car_offer_premium(i18n: TranslatorHub,
                                   **kwargs) -> dict[str, str]:
    car_offer_premium_text = i18n.car.offer.premium.text(
        premium_price=PREMIUM_PRICE
    )

    return {"car_offer_premium_text": car_offer_premium_text,
            "connect_premium_button": i18n.connect.premium.button(),
            "back_button": i18n.back.button(),
            "home_button": i18n.home.button()}
