from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import HomeState, GarageState, ServiceRecordState, LkStates


async def home_write_developer(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=HomeState.write_developer)


async def home_instructions(callback: CallbackQuery,
                            button: Button,
                            dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=HomeState.instructions)


async def home_get_instruction(callback: CallbackQuery,
                               widget: Select,
                               dialog_manager: DialogManager,
                               item_id: str):
    dialog_manager.dialog_data.update(instr_id=item_id)

    await dialog_manager.switch_to(state=HomeState.get_instruction)


async def home_garage(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    await dialog_manager.start(state=GarageState.home)


async def home_add_param(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    await dialog_manager.start(state=HomeState.select_record)


async def home_service_record(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    await dialog_manager.start(state=ServiceRecordState.home)


async def home_lk(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    await dialog_manager.start(state=LkStates.home)
