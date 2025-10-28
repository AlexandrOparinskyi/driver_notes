from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select, Calendar
from aiogram_dialog.widgets.text import Format

from bot.states import ServiceRecordState
from .filters import service_record_check_text
from .getters import (getter_service_record_home,
                      getter_service_record_edit_btn,
                      getter_service_record_edit_txt,
                      getter_service_record_edit_date)
from .handlers import (service_record_back_to_select,
                       service_record_back_to_select_part,
                       service_record_edit_part,
                       service_record_save_selected_part,
                       service_record_save_enter_part,
                       service_record_save_select_date,
                       service_record_save_button)
from ..general import (service_in_development,
                       generale_message_not_text)

service_record_dialog = Dialog(
    Window(
        Format("{service_record_home_text}"),
        Button(text=Format("{add_part_button}"),
               id="add_part_button",
               on_click=service_in_development),
        Button(text=Format("{add_work_button}"),
               id="add_work_button",
               on_click=service_in_development),
        Group(Select(text=Format("{item[0]}"),
                     id="select_service_record_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=service_record_edit_part),
              width=2),
        Button(text=Format("{save_button}"),
               id="save_button",
               on_click=service_record_save_button),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_record_back_to_select),
        getter=getter_service_record_home,
        state=ServiceRecordState.home
    ),
    Window(
        Format("{edit_service_part_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="service_car_or_type",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=service_record_save_selected_part),
              width=2),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_record_back_to_select_part),
        getter=getter_service_record_edit_btn,
        state=ServiceRecordState.edit_button
    ),
    Window(
        Format("{edit_service_part_text}"),
        MessageInput(func=service_record_save_enter_part,
                     content_types=ContentType.TEXT,
                     filter=service_record_check_text),
        MessageInput(func=generale_message_not_text,
                     content_types=[ContentType.VIDEO,
                                    ContentType.PHOTO,
                                    ContentType.DOCUMENT,
                                    ContentType.STICKER]),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_record_back_to_select_part),
        getter=getter_service_record_edit_txt,
        state=ServiceRecordState.edit_text
    ),
    Window(
        Format("{edit_service_part_text}"),
        Calendar(id="service_record_calendar",
                 on_click=service_record_save_select_date),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_record_back_to_select_part),
        getter=getter_service_record_edit_date,
        state=ServiceRecordState.calendar
    )
)
