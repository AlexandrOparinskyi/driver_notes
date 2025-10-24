from datetime import datetime

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id, get_car_by_id
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


async def getter_car_detail(i18n: TranslatorHub,
                            dialog_manager: DialogManager,
                            **kwargs) -> dict[str, str]:
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)

    total_expenses = 0
    total_records = 0
    car_mileage = car.mileage if car.mileage else 0
    days_owned = (datetime.now() - car.created_at).days
    car_detail_text = i18n.car.details.text(car_name=car.name,
                                            total_expenses=total_expenses,
                                            total_records=total_records,
                                            car_mileage=car_mileage,
                                            days_owned=days_owned,
                                            recent_activities="None")

    return {"car_detail_text": car_detail_text,
            "back_button": i18n.back.button()}
