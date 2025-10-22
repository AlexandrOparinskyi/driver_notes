from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format

from bot.states import StartState
from .getters import (getter_start,
                      getter_start_acquaintance,
                      getter_start_car_name,
                      getter_completed_car_name,
                      getter_start_confirm)
from .handlers import (start_acquaintance_button,
                       start_add_car_button,
                       start_enter_car_name,
                       start_car_menu)
from ..general import (generale_message_not_text,
                       home_button)

start_dialog = Dialog(
    Window(
        Format("{start_text}"),
        Button(text=Format("{start_acquaintance_button}"),
               id="start_acquaintance_button",
               on_click=start_acquaintance_button),
        getter=getter_start,
        state=StartState.start
    ),
    Window(
        Format("{start_acquaintance_text}"),
        Button(text=Format("{add_car_button}"),
               id="add_car_button",
               on_click=start_add_car_button),
        getter=getter_start_acquaintance,
        state=StartState.acquaintance
    ),
    Window(
        Format("{start_car_name_text}"),
        MessageInput(func=start_enter_car_name,
                     content_types=ContentType.TEXT),
        MessageInput(func=generale_message_not_text),
        getter=getter_start_car_name,
        state=StartState.car_name
    ),
    Window(
        Format("{start_completed_car_name_text}"),
        Button(text=Format("{car_menu_button}"),
               id="car_menu_button",
               on_click=start_car_menu),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_completed_car_name,
        state=StartState.completed_car_name
    ),
    Window(
        Format("{start_confirm_text}"),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_start_confirm,
        state=StartState.confirm
    )
)
