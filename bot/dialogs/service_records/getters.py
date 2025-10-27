from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils.service_record import (get_button_for_add_service_record,
                                      get_text_for_service_data)


async def getter_service_record_home(i18n: TranslatorHub,
                                     dialog_manager: DialogManager,
                                     event_from_user: User,
                                     **kwargs) -> dict[str, str | list]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    service_data = await get_text_for_service_data(
        i18n,
        event_from_user.id,
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
            "add_work_button": i18n.service.add.work.button()}
