from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils.service_work import (get_buttons_for_edit_service_work,
                                    get_text_for_work_data,
                                    get_text_for_edit_work_param)


async def getter_service_work_enter_name(i18n: TranslatorHub,
                                         dialog_manager: DialogManager,
                                         **kwargs) -> dict[str, str]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    return {"add_work_text": i18n.service.work.enter.name.text(),
            "back_button": i18n.back.button()}


async def getter_service_work_home(i18n: TranslatorHub,
                                   dialog_manager: DialogManager,
                                   **kwargs) -> dict[str, str | list]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    work_data = dialog_manager.dialog_data.get("work_data")
    selected_work = dialog_manager.dialog_data.get("selected_work")
    num_selected_work = int(selected_work.split("_")[1]) + 1
    part_text = get_text_for_work_data(i18n, work_data[selected_work])

    service_work_home_text = i18n.service.work.edit.menu.text(
        work_num=num_selected_work,
        work_data=part_text
    )
    buttons = get_buttons_for_edit_service_work(i18n)
    count_button = f"{num_selected_work}/{len(work_data)}"

    return {"service_work_home_text": service_work_home_text,
            "back_button": i18n.back.button(),
            "buttons": buttons,
            "next_button": ">>",
            "prev_button": "<<",
            "count_button": count_button,
            "delete_button": i18n.service.part.delete.button(),
            "add_work_button": i18n.service.work.add.button()}


async def getter_service_work_edit_param(i18n: TranslatorHub,
                                         dialog_manager: DialogManager,
                                         **kwargs) -> dict[str, str]:
    work_param = dialog_manager.dialog_data.get("work_param")
    text = get_text_for_edit_work_param(i18n, work_param)

    return {"edit_work_param_text": text,
            "back_button": i18n.back.button()}
