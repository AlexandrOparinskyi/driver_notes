from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, Button

from bot.states import CarState, StartState, HomeState
from bot.utils import (get_car_mark_by_id,
                       get_car_model_by_id, update_car_by_id)


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


async def car_select_part(callback: CallbackQuery,
                          widget: Select,
                          dialog_manager: DialogManager,
                          item_id: str):
    car_part = dialog_manager.dialog_data.get("car_part")

    dialog_manager.dialog_data[car_part] = item_id

    if car_part == "car_mark":
        mark = await get_car_mark_by_id(int(item_id))
        dialog_manager.dialog_data[car_part] = mark.name
        dialog_manager.dialog_data.update(mark_id=item_id)

    if car_part == "car_model":
        model = await get_car_model_by_id(int(item_id))
        dialog_manager.dialog_data[car_part] = model.name
        dialog_manager.dialog_data.update(model_id=item_id,
                                          mark_id=model.mark_id)
        if not dialog_manager.dialog_data.get("car_mark"):
            dialog_manager.dialog_data.update(car_mark=model.mark.name)

    await dialog_manager.switch_to(state=CarState.home)


async def car_enter_part(message: Message,
                         widget: MessageInput,
                         dialog_manager: DialogManager):
    car_part = dialog_manager.dialog_data.get("car_part")

    dialog_manager.dialog_data[car_part] = message.text

    await dialog_manager.switch_to(state=CarState.home)


async def car_save(callback: CallbackQuery,
                   button: Button,
                   dialog_manager: DialogManager):
    await update_car_by_id(user_id=callback.from_user.id,
                           **dialog_manager.dialog_data)

    if dialog_manager.dialog_data.get("is_first_car"):
        await dialog_manager.start(state=StartState.confirm)
        return

    await dialog_manager.start(state=HomeState.home)
