from datetime import datetime

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id, get_car_by_id, get_car_smile
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
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)
    smile = get_car_smile()

    total_expenses = 0
    total_records = 0
    car_mileage = car.mileage if car.mileage else 0
    days_owned = (datetime.now() - car.created_at).days
    car_detail_text = i18n.car.details.text(car_name=f"{smile} {car.name}",
                                            total_expenses=total_expenses,
                                            total_records=total_records,
                                            car_mileage=car_mileage,
                                            days_owned=days_owned,
                                            recent_activities="None")

    return {"car_detail_text": car_detail_text,
            "back_button": i18n.back.button(),
            "edit_name_button": i18n.edit.car.name.button(),
            "edit_data_button": i18n.edit.car.data.button(),
            "edit_documents_button": i18n.edit.car.documents.button(),
            "get_report_button": i18n.car.report.button(),
            "setting_notification_button": i18n.setting.notification.button(),
            "delete_car_button": i18n.delete.car.button()}
