from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format

from bot.states import GarageState
from .getters import getter_garage
from ..general import home_button

garage_dialog = Dialog(
    Window(
        Format("{garage_text}"),
        Button(text=Format("{add_car_button}"),
               id="add_car_button",
               on_click=None),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_garage,
        state=GarageState.home
    )
)
