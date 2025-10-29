from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select, Row
from aiogram_dialog.widgets.text import Format

from bot.states import ServicePartState
from .filters import service_part_check_text
from .getters import (getter_service_part_home,
                      getter_service_part_enter_name,
                      getter_service_part_edit_param)
from .handlers import (service_part_back_to_record,
                       service_part_select_param,
                       service_part_enter_name,
                       service_part_back_to_home,
                       service_part_enter_param,
                       service_part_next_button,
                       service_part_prev_button,
                       service_part_delete_button,
                       service_part_add_part_button)
from ..general import generale_message_not_text

service_part_dialog = Dialog(
    Window(
        Format("{add_part_text}"),
        MessageInput(func=service_part_enter_name,
                     content_types=ContentType.TEXT),
        MessageInput(func=generale_message_not_text,
                     content_types=[ContentType.VIDEO,
                                    ContentType.PHOTO,
                                    ContentType.DOCUMENT,
                                    ContentType.STICKER]),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_part_back_to_record),
        getter=getter_service_part_enter_name,
        state=ServicePartState.enter_name
    ),
    Window(
        Format("{service_part_home_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="select_edit_service_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=service_part_select_param),
              width=2),
        Button(text=Format("{delete_button}"),
               id="delete_button",
               on_click=service_part_delete_button),
        Row(Button(text=Format("{prev_button}"),
                   id="prev_button",
                   on_click=service_part_prev_button),
            Button(text=Format("{count_button}"),
                   id="count_button",
                   on_click=None),
            Button(text=Format("{next_button}"),
                   id="next_button",
                   on_click=service_part_next_button),
            ),
        Button(text=Format("{add_part_button}"),
               id="add_part_button",
               on_click=service_part_add_part_button),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_part_back_to_record),
        getter=getter_service_part_home,
        state=ServicePartState.home
    ),
    Window(
        Format("{edit_part_param_text}"),
        MessageInput(func=service_part_enter_param,
                     content_types=ContentType.TEXT,
                     filter=service_part_check_text),
        MessageInput(func=generale_message_not_text,
                     content_types=[ContentType.VIDEO,
                                    ContentType.PHOTO,
                                    ContentType.DOCUMENT,
                                    ContentType.STICKER]),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_part_back_to_home),
        getter=getter_service_part_edit_param,
        state=ServicePartState.edit_param
    )
)
