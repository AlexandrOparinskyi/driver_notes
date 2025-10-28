from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import get_buttons_for_edit_service_part, get_text_for_part_data


async def getter_service_part_home(i18n: TranslatorHub,
                                   dialog_manager: DialogManager,
                                   **kwargs) -> dict[str, str | list]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    if not dialog_manager.dialog_data.get("part_num"):
        dialog_manager.dialog_data.update(part_num=0)
        part_num = 1
    else:
        part_num = int(dialog_manager.dialog_data.get("part_num")) + 1

    try:
        part_dict = dialog_manager.dialog_data.get("part_dict")[part_num]
    except TypeError:
        part_dict = {part_num: {}}
        dialog_manager.dialog_data.update(part_dict=part_dict)

    part_data = get_text_for_part_data(i18n, part_dict)

    service_part_home_text = i18n.service.part.edit.menu.text(
        part_num=part_num,
        part_data=part_data
    )
    buttons = get_buttons_for_edit_service_part(i18n)

    return {"service_part_home_text": service_part_home_text,
            "back_button": i18n.back.button(),
            "buttons": buttons}


async def getter_service_part_edit_param(i18n: TranslatorHub,
                                         **kwargs) -> dict[str, str]
