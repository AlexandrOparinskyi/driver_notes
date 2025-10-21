from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Group, Select, Button
from aiogram_dialog.widgets.text import Format

from .getters import (getter_car_home,
                      getter_edit_part)
from bot.states import CarState
from .handlers import (car_edit_part,
                       car_back_button_home)

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
               on_click=None),
        getter=getter_car_home,
        state=CarState.home
    ),
    Window(
        Format("{car_edit_part_text}"),
        Group(Select(text=Format("{item[0]}"),
                     id="car_edit_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=None),
              width=3),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=car_back_button_home),
        getter=getter_edit_part,
        state=CarState.edit_part
    )
)
