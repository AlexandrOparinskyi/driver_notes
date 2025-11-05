from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Select, Button, Calendar
from aiogram_dialog.widgets.text import Format

from bot.states import CarState, CarDataState
from .filters import car_check_enter_part
from .getters import (getter_car_home,
                      getter_edit_part,
                      getter_edit_car_name,
                      getter_car_data_home,
                      getter_car_data_edit_docs,
                      getter_car_data_calendar)
from .handlers import (car_edit_part,
                       car_back_button_home,
                       car_select_part,
                       car_enter_part,
                       car_save,
                       car_rename,
                       back_button_to_garage,
                       back_button_to_car_documents,
                       edit_car_data,
                       enter_car_document,
                       select_date_insurance)
from ..general import generale_message_not_text

edit_car_dialog = Dialog(
    Window(
        Format("{car_edit_menu_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="car_data",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=car_edit_part),
              width=2),
        Button(text=Format("{save_button}"),
               id="save_button",
               on_click=car_save),
        getter=getter_car_home,
        state=CarState.home
    ),
    Window(
        Format("{car_edit_part_text}"),
        MessageInput(func=car_enter_part,
                     content_types=ContentType.TEXT,
                     filter=car_check_enter_part),
        MessageInput(func=generale_message_not_text,
                     content_types=(ContentType.PHOTO,
                                    ContentType.VIDEO,
                                    ContentType.STICKER,
                                    ContentType.DOCUMENT)),
        Group(Select(text=Format("{item[0]}"),
                     id="car_edit_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=car_select_part),
              width=3),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=car_back_button_home),
        getter=getter_edit_part,
        state=CarState.edit_part
    ),
    Window(
        Format("{car_rename_text}"),
        MessageInput(func=car_rename,
                     content_types=ContentType.TEXT),
        MessageInput(func=generale_message_not_text),
        Button(text=Format("{cancel_button}"),
               id="cancel_button",
               on_click=back_button_to_garage),
        getter=getter_edit_car_name,
        state=CarState.edit_car_name
    )
)

car_data_dialog = Dialog(
    Window(
        Format("{data_documents_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="car_doc_buttons",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=edit_car_data),
              width=3),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=back_button_to_garage),
        getter=getter_car_data_home,
        state=CarDataState.home,
    ),
    Window(
        Format("{edit_car_doc_text}"),
        MessageInput(func=enter_car_document,
                     content_types=ContentType.TEXT),
        MessageInput(func=generale_message_not_text),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=back_button_to_car_documents),
        getter=getter_car_data_edit_docs,
        state=CarDataState.edit_documents
    ),
    Window(
        Format("{date_text}"),
        Calendar(id="insurance_calendar",
                 on_click=select_date_insurance),
        Button(text=Format("{skip_button}"),
               id="skip_button",
               on_click=back_button_to_car_documents),
        getter=getter_car_data_calendar,
        state=CarDataState.calendar
    )
)
