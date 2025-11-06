from datetime import datetime

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import (get_user_by_id,
                       get_car_by_id,
                       get_car_smile,
                       get_last_records,
                       get_car_record_buttons_to_dict, get_record_text)
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

    total_expenses = car.get_total_price
    total_records = len(car.service_records)
    car_mileage = car.mileage if car.mileage else 0
    days_owned = (datetime.now() - car.created_at).days
    recent_activities = get_last_records(i18n,
                                         car.get_records(),
                                         3)
    car_detail_text = i18n.car.details.text(
        car_name=f"{smile} {car.name}",
        total_expenses=total_expenses,
        total_records=total_records,
        car_mileage=car_mileage,
        days_owned=days_owned,
        recent_activities=recent_activities
    )

    return {"car_detail_text": car_detail_text,
            "back_button": i18n.back.button(),
            "edit_name_button": i18n.edit.car.name.button(),
            "edit_data_button": i18n.edit.car.data.button(),
            "edit_documents_button": i18n.edit.car.documents.button(),
            "get_report_button": i18n.car.report.button(),
            "setting_notification_button": i18n.setting.notification.button(),
            "delete_car_button": i18n.delete.car.button()}


async def getter_car_records(i18n: TranslatorHub,
                             dialog_manager: DialogManager,
                             **kwargs) -> dict[str, str | list]:
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)
    service = dialog_manager.dialog_data.get("checked_service_filter")
    if service is None:
        service = True
    refuel = dialog_manager.dialog_data.get("checked_refuel_filter")
    purchase = dialog_manager.dialog_data.get("checked_purchase_filter")
    other = dialog_manager.dialog_data.get("checked_other_filter")
    records = car.get_records(service,
                              refuel if refuel else False,
                              purchase if purchase else False,
                              other if other else False)

    text = i18n.car.records.text(car_name=car.name,
                                 records_count=len(records))
    n = dialog_manager.dialog_data.get("n")
    record_buttons = get_car_record_buttons_to_dict(i18n, records, 6)
    dialog_manager.dialog_data.update(len_records=len(record_buttons))
    try:
        buttons = record_buttons[n]
    except KeyError:
        buttons = []

    prev_button = "<<"
    next_button = ">>"
    len_records = len(record_buttons) if len(record_buttons) else 1
    count_button = f"{int(n.split('_')[1]) + 1}/{len_records}"

    return {"car_record_text": text,
            "back_button": i18n.back.button(),
            "active_service_button": i18n.active.service.button(),
            "active_refuel_button": i18n.active.refuel.button(),
            "active_purchase_button": i18n.active.purchase.button(),
            "active_other_button": i18n.active.other.button(),
            "unactive_service_button": i18n.unactive.service.button(),
            "unactive_refuel_button": i18n.unactive.refuel.button(),
            "unactive_purchase_button": i18n.unactive.purchase.button(),
            "unactive_other_button": i18n.unactive.other.button(),
            "record_buttons": buttons,
            "prev_button": prev_button,
            "next_button": next_button,
            "count_button": count_button}


async def getter_garage_record(i18n: TranslatorHub,
                               dialog_manager: DialogManager,
                               **kwargs) -> dict[str, str]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    record_type = dialog_manager.dialog_data.get("record_type")
    record_id = int(dialog_manager.dialog_data.get("record_id"))

    text = await get_record_text(i18n, record_type, record_id)

    download_button = ""
    if record_type == "service":
        download_button = i18n.garage.download.record.button()

    return {"record_text": text,
            "back_button": i18n.back.button(),
            "download_button": download_button,
            "edit_button": i18n.garage.edit.record.button(),
            "delete_button": i18n.garage.delete.record.button()}
