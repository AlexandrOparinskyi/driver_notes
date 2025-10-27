from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


async def service_record_back_to_select(callback: CallbackQuery,
                                        button: Button,
                                        dialog_manager: DialogManager):
    await dialog_manager.done()
