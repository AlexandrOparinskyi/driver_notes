from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Group, Select
from aiogram_dialog.widgets.text import Format

from bot.states import ServicePartState
from .getters import getter_service_part_home
from .handlers import (service_part_back_to_record,
                       service_part_select_param)

service_part_dialog = Dialog(
    Window(
        Format("{service_part_home_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="select_edit_service_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=service_part_select_param),
              width=2),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_part_back_to_record),
        getter=getter_service_part_home,
        state=ServicePartState.home
    ),
    Window(
        state=ServicePartState.edit_param
    )
)
