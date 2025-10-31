from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils.refuel_record import (get_buttons_for_edit_refuel_record,
                                     get_text_for_refuel_data,
                                     get_text_for_edit_refuel_record_param, get_buttons_for_edit_refuel)


async def getter_refuel_record_enter_price(i18n: TranslatorHub,
                                           **kwargs) -> dict[str, str]:
    return {"enter_price_text": i18n.refuel.record.enter.price.text(),
            "back_button": i18n.back.button()}


async def getter_refuel_record_home(i18n: TranslatorHub,
                                    dialog_manager: DialogManager,
                                    **kwargs) -> dict[str, str | list]:
    refuel_data = await get_text_for_refuel_data(i18n,
                                                 dialog_manager.dialog_data)

    home_text = i18n.refuel.record.home.text(refuel_data=refuel_data)
    buttons = get_buttons_for_edit_refuel_record(i18n)


    return {"home_text": home_text,
            "save_button": i18n.save.button(),
            "buttons": buttons,
            "home_button": i18n.home.button(),
            "full_tank_button": i18n.refuel.record.full.tank.button(),
            "no_full_tank_button": i18n.refuel.record.no.full.tank.button()}


async def getter_refuel_record_edit_param(i18n: TranslatorHub,
                                          dialog_manager: DialogManager,
                                          event_from_user: User,
                                          **kwargs) -> dict[str, str | list]:
    refuel_part = dialog_manager.dialog_data.get("refuel_part")

    text = get_text_for_edit_refuel_record_param(i18n, refuel_part)
    buttons = await get_buttons_for_edit_refuel(i18n,
                                                refuel_part,
                                                event_from_user.id)

    return {"edit_text": text,
            "back_button": i18n.back.button(),
            "buttons": buttons}


async def getter_refuel_record_calendar(i18n: TranslatorHub,
                                        **kwargs) -> dict[str, str]:
    return {"edit_date_text": i18n.refuel.record.edit.date.text(),
            "back_button": i18n.back.button()}
