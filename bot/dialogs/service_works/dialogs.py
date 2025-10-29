from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select, Row
from aiogram_dialog.widgets.text import Format

from bot.states import ServiceWorkState
from .filters import service_work_check_text
from .getters import (getter_service_work_home,
                      getter_service_work_enter_name,
                      getter_service_work_edit_param)
from .handlers import (service_work_back_to_record,
                       service_work_enter_name,
                       service_work_back_to_home,
                       service_work_select_param,
                       service_work_enter_param,
                       service_work_next_button,
                       service_work_prev_button,
                       service_work_add_work_button,
                       service_work_delete_button)
from ..general import generale_message_not_text

service_work_dialog = Dialog(
    Window(
        Format("{add_work_text}"),
        MessageInput(func=service_work_enter_name,
                     content_types=ContentType.TEXT),
        MessageInput(func=generale_message_not_text,
                     content_types=[ContentType.VIDEO,
                                    ContentType.PHOTO,
                                    ContentType.DOCUMENT,
                                    ContentType.STICKER]),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_work_back_to_record),
        getter=getter_service_work_enter_name,
        state=ServiceWorkState.enter_name
    ),
    Window(
        Format("{service_work_home_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="select_edit_service_work",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=service_work_select_param),
              Button(text=Format("{delete_button}"),
                     id="delete_button",
                     on_click=service_work_delete_button),
              width=2),
        Row(Button(text=Format("{prev_button}"),
                   id="prev_button",
                   on_click=service_work_prev_button),
            Button(text=Format("{count_button}"),
                   id="count_button",
                   on_click=None),
            Button(text=Format("{next_button}"),
                   id="next_button",
                   on_click=service_work_next_button),
            ),
        Button(text=Format("{add_work_button}"),
               id="add_work_button",
               on_click=service_work_add_work_button),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_work_back_to_record),
        getter=getter_service_work_home,
        state=ServiceWorkState.home
    ),
    Window(
        Format("{edit_work_param_text}"),
        MessageInput(func=service_work_enter_param,
                     content_types=ContentType.TEXT,
                     filter=service_work_check_text),
        MessageInput(func=generale_message_not_text,
                     content_types=[ContentType.VIDEO,
                                    ContentType.PHOTO,
                                    ContentType.DOCUMENT,
                                    ContentType.STICKER]),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_work_back_to_home),
        getter=getter_service_work_edit_param,
        state=ServiceWorkState.edit_param
    )
)
