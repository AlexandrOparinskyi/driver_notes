from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format

from bot.states import StartState
from .getters import getter_start

start_dialog = Dialog(
    Window(
        Format("{start_text}"),
        Button(text=Format("{start_acquaintance_button}"),
               id="start_acquaintance_button",
               on_click=None),
        getter=getter_start,
        state=StartState.start
    )
)
