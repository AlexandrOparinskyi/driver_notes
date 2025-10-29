from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import (get_buttons_for_edit_service_part,
                       get_text_for_part_data,
                       get_text_for_edit_part_param)


async def getter_service_part_enter_name(i18n: TranslatorHub,
                                         dialog_manager: DialogManager,
                                         **kwargs) -> dict[str, str]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    return {"add_part_text": i18n.service.part.add.name.text(),
            "back_button": i18n.back.button()}


async def getter_service_part_home(i18n: TranslatorHub,
                                   dialog_manager: DialogManager,
                                   **kwargs) -> dict[str, str | list]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    part_data = dialog_manager.dialog_data.get("part_data")
    selected_part = dialog_manager.dialog_data.get("selected_part")
    num_selected_part = int(selected_part.split("_")[1]) + 1
    part_text = get_text_for_part_data(i18n, part_data[selected_part])

    service_part_home_text = i18n.service.part.edit.menu.text(
        part_num=num_selected_part,
        part_data=part_text
    )
    buttons = get_buttons_for_edit_service_part(i18n)
    count_button = f"{num_selected_part}/{len(part_data)}"

    return {"service_part_home_text": service_part_home_text,
            "back_button": i18n.back.button(),
            "buttons": buttons,
            "next_button": ">>",
            "prev_button": "<<",
            "count_button": count_button,
            "delete_button": i18n.service.part.delete.button(),
            "add_part_button": i18n.service.part.add.button()}


async def getter_service_part_edit_param(i18n: TranslatorHub,
                                         dialog_manager: DialogManager,
                                         **kwargs) -> dict[str, str]:
    part_param = dialog_manager.dialog_data.get("part_param")
    text = get_text_for_edit_part_param(i18n, part_param)

    return {"edit_part_param_text": text,
            "back_button": i18n.back.button()}
