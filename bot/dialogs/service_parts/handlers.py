from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import ServiceRecordState, ServicePartState


async def service_part_back_to_record(callback: CallbackQuery,
                                      button: Button,
                                      dialog_manager: DialogManager):
    await dialog_manager.start(state=ServiceRecordState.home,
                               data=dialog_manager.dialog_data)


async def service_part_select_param(callback: CallbackQuery,
                                    widget: Select,
                                    dialog_manager: DialogManager,
                                    item_id: str):
    dialog_manager.dialog_data.update(part_param=item_id)

    await dialog_manager.switch_to(state=ServicePartState.edit_param)
