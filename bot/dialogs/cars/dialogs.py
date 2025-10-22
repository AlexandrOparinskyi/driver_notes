from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Select, Button
from aiogram_dialog.widgets.text import Format

from .filters import car_check_enter_part
from .getters import (getter_car_home,
                      getter_edit_part)
from bot.states import CarState
from .handlers import (car_edit_part,
                       car_back_button_home,
                       car_select_part,
                       car_enter_part,
                       car_save)
from ..general import generale_message_not_text

add_car_dialog = Dialog(
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
    )
)
