from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select, Checkbox, Calendar
from aiogram_dialog.widgets.text import Format

from bot.states import RefuelRecordState
from .filters import (refuel_record_check_price,
                      refuel_record_check_part)
from .getters import (getter_refuel_record_enter_price,
                      getter_refuel_record_home,
                      getter_refuel_record_calendar,
                      getter_refuel_record_edit_param)
from .handlers import (refuel_record_back_to_select_record,
                       refuel_record_enter_price,
                       refuel_record_full_tank_checkbox,
                       refuel_record_edit_param,
                       refuel_record_back_to_home,
                       refuel_record_edit_date,
                       refuel_record_edit_part,
                       refuel_record_enter_part,
                       refuel_record_save,
                       refuel_record_back_to_record)
from ..general import (generale_message_not_text,
                       home_button)

refuel_record_dialog = Dialog(
    Window(
        Format("{enter_price_text}"),
        MessageInput(func=refuel_record_enter_price,
                     content_types=ContentType.TEXT,
                     filter=refuel_record_check_price),
        MessageInput(func=generale_message_not_text,
                     content_types=[ContentType.VIDEO,
                                    ContentType.PHOTO,
                                    ContentType.DOCUMENT,
                                    ContentType.STICKER]),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=refuel_record_back_to_select_record),
        getter=getter_refuel_record_enter_price,
        state=RefuelRecordState.enter_price
    ),
    Window(
        Format("{home_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="select_refuel_record_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=refuel_record_edit_param),
              Checkbox(checked_text=Format("{full_tank_button}"),
                       unchecked_text=Format("{no_full_tank_button}"),
                       id="full_tank_checkbox",
                       default=False,
                       on_state_changed=refuel_record_full_tank_checkbox),
              width=2),
        Button(text=Format("{save_button}"),
               id="save_button",
               on_click=refuel_record_save),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=refuel_record_back_to_record),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_refuel_record_home,
        state=RefuelRecordState.home
    ),
    Window(
        Format("{edit_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="select_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=refuel_record_edit_part),
              width=2),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=refuel_record_back_to_home),
        getter=getter_refuel_record_edit_param,
        state=RefuelRecordState.edit_button
    ),
    Window(
        Format("{edit_text}"),
        MessageInput(func=refuel_record_enter_part,
                     content_types=ContentType.TEXT,
                     filter=refuel_record_check_part),
        MessageInput(func=generale_message_not_text,
                     content_types=[ContentType.VIDEO,
                                    ContentType.PHOTO,
                                    ContentType.DOCUMENT,
                                    ContentType.STICKER]),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=refuel_record_back_to_home),
        getter=getter_refuel_record_edit_param,
        state=RefuelRecordState.edit_text
    ),
    Window(
        Format("{edit_date_text}"),
        Calendar(id="refuel_record_calendar",
                 on_click=refuel_record_edit_date),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=refuel_record_back_to_home),
        getter=getter_refuel_record_calendar,
        state=RefuelRecordState.calendar
    )
)
