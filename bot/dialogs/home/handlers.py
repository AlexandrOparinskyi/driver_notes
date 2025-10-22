from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states import HomeState


async def home_write_developer(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=HomeState.write_developer)


async def home_instructions(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=HomeState.instructions)
