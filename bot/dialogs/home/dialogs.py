from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from bot.states import HomeState

home_dialog = Dialog(
    Window(
        Format("Home"),
        state=HomeState.home
    )
)
