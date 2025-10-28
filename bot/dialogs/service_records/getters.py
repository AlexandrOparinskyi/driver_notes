from datetime import datetime

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import (get_user_by_id,
                       get_button_for_add_service_record,
                       get_text_for_service_data,
                       get_button_for_edit_service_car,
                       get_button_for_edit_service_type,
                       get_text_for_edit_service_record_part)


async def getter_service_record_home(i18n: TranslatorHub,
                                     dialog_manager: DialogManager,
                                     event_from_user: User,
                                     **kwargs) -> dict[str, str | list]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    if not dialog_manager.dialog_data.get("service_car"):
        user = await get_user_by_id(event_from_user.id)
        car = user.get_main_car
        if car:
            dialog_manager.dialog_data.update(service_car=car.id)

    if not dialog_manager.dialog_data.get("service_date"):
        dialog_manager.dialog_data.update(service_date=datetime.now())

    service_data = await get_text_for_service_data(
        i18n,
        dialog_manager.dialog_data
    )
    service_record_home_text = i18n.service.record.home.text(
        service_data=service_data
    )
    buttons = get_button_for_add_service_record(i18n)

    return {"service_record_home_text": service_record_home_text,
            "back_button": i18n.back.button(),
            "buttons": buttons,
            "add_part_button": i18n.service.add.part.button(),
            "add_work_button": i18n.service.add.work.button(),
            "save_button": i18n.save.button()}


async def getter_service_record_edit_btn(i18n: TranslatorHub,
                                         dialog_manager: DialogManager,
                                         event_from_user: User,
                                         **kwargs) -> dict[str, str | list]:
    service_part = dialog_manager.dialog_data.get("service_part")
    text = i18n.service.record.error.part.text()
    buttons = None

    if service_part == "service_car":
        text = i18n.service.record.edit.car.text()
        buttons = await get_button_for_edit_service_car(event_from_user.id)

    if service_part == "service_type":
        text = i18n.service.record.edit.type.text()
        buttons = get_button_for_edit_service_type()

    return {"edit_service_part_text": text,
            "buttons": buttons,
            "back_button": i18n.back.button()}


async def getter_service_record_edit_txt(i18n: TranslatorHub,
                                         dialog_manager: DialogManager,
                                         event_from_user: User,
                                         **kwargs) -> dict[str, str]:
    service_part = dialog_manager.dialog_data.get("service_part")
    text = get_text_for_edit_service_record_part(i18n, service_part)

    return {"edit_service_part_text": text,
            "back_button": i18n.back.button()}


async def getter_service_record_edit_date(i18n: TranslatorHub,
                                          **kwargs) -> dict[str, str]:
    return {"edit_service_part_text": i18n.service.record.edit.date.text(),
            "back_button": i18n.back.button()}
