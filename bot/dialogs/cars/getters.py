from aiogram_dialog import DialogManager
from asyncpg.pgproto.pgproto import timedelta
from fluentogram import TranslatorHub

from bot.utils import (get_car_by_id,
                       get_button_for_add_car,
                       get_text_for_edit_part,
                       get_button_for_edit_car,
                       get_text_for_car_data, get_buttons_for_edit_car_data, get_text_for_edit_car_doc_data)


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
            "save_button": i18n.save.button()}


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
                               **kwargs) -> dict[str, str | list]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)
        dialog_manager.start_data.clear()

    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)

    field_no_filled = i18n.field.no.filled()
    vin = (f"✅ <code>{car.car_documents.vin_number}</code>"
           if car.car_documents.vin_number else field_no_filled)
    sts = (f"✅ <code>{car.car_documents.sts}</code>"
           if car.car_documents.sts else field_no_filled)
    pts = (f"✅ <code>{car.car_documents.pts}</code>"
                  if car.car_documents.pts else field_no_filled)
    insurance = (f"✅ <code>{car.car_documents.insurance_number}</code>"
                  if car.car_documents.insurance_number else field_no_filled)
    gos_number = (f"✅ <code>{car.car_documents.gos_number}</code>"
                  if car.car_documents.gos_number else field_no_filled)

    data_documents_text = i18n.car.documents.text(
        car_name=car.name,
        vin=vin,
        car_number=gos_number,
        sts=sts,
        pts=pts,
        insurance_number=insurance,
        insurance_days="В разработке..."
    )
    buttons = get_buttons_for_edit_car_data(i18n)

    return {"data_documents_text": data_documents_text,
            "back_button": i18n.back.button(),
            "buttons": buttons}


async def getter_car_data_edit_docs(i18n: TranslatorHub,
                                    dialog_manager: DialogManager,
                                    **kwargs) -> dict[str, str]:
    car_doc = dialog_manager.dialog_data.get("car_doc")
    text = get_text_for_edit_car_doc_data(i18n, car_doc)

    return {"edit_car_doc_text": text,
            "back_button": i18n.back.button()}


async def getter_car_data_calendar(i18n: TranslatorHub,
                                   **kwargs) -> dict[str, str]:
    return {"date_text": i18n.car.doc.add.osago.date.text(),
            "skip_button": i18n.skip.button()}
