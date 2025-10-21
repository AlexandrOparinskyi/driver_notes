from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from bot.states import CarState


async def car_edit_part(callback: CallbackQuery,
                        widget: Select,
                        dialog_manager: DialogManager,
                        item_id: str):
    dialog_manager.dialog_data.update(car_part=item_id)

    await dialog_manager.switch_to(state=CarState.edit_part)


async def car_back_button_home(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=CarState.home)
