from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import (get_car_by_id,
                       get_button_for_add_car,
                       get_text_for_edit_part,
                       get_button_for_edit_car,
                       get_text_for_car_data)


async def getter_car_home(i18n: TranslatorHub,
                          dialog_manager: DialogManager,
                          **kwargs) -> dict[str, str | list]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)
    buttons = get_button_for_add_car(i18n)
    car_data = get_text_for_car_data(dialog_manager.dialog_data)

    return {"car_edit_menu_text": i18n.car.edit.menu.text(car_name=car.name,
                                                          car_data=car_data),
            "buttons": buttons,
            "save_button": i18n.car.save.button()}


async def getter_edit_part(i18n: TranslatorHub,
                           dialog_manager: DialogManager,
                           **kwargs) -> dict[str, str | list]:
    car_part = dialog_manager.dialog_data.get("car_part")
    text = get_text_for_edit_part(i18n, car_part)
    buttons = await get_button_for_edit_car(
        i18n,
        car_part,
        dialog_manager.dialog_data.get("mark_id")
    )

    return {"car_edit_part_text": text,
            "buttons": buttons,
            "back_button": i18n.back.button()}


async def getter_edit_car_name(i18n: TranslatorHub,
                               **kwargs) -> dict[str, str]:
    return {"car_rename_text": i18n.car.rename.text(),
            "cancel_button": i18n.cancel.button()}


async def getter_car_data_home(i18n: TranslatorHub,
                               dialog_manager: DialogManager,
                               **kwargs) -> dict[str, str]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)

    field_no_filled = i18n.field.no.filled()
    spoiler = f"{field_no_filled}"

    data_documents_text = i18n.car.documents.text(
        car_name=car.name,
        vin=spoiler,
        car_number=field_no_filled,
        sts=field_no_filled,
        pts=field_no_filled,
        insurance_number=field_no_filled,
        insurance_days=0
    )

    return {"data_documents_text": data_documents_text,
            "back_button": i18n.back.button(),
            "add_documents_button": i18n.add.documents.button()}


async def getter_edit_car_data(i18n: TranslatorHub,
                               dialog_manager: DialogManager,
                               **kwargs) -> dict[str, str]:
    pass
