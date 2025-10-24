from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.states import GarageState, CarState
from bot.utils import create_car
from config import CURRENT_CAR_NAME_LENGTH


async def garage_add_car(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=GarageState.car_name)


async def back_button_to_garage(callback: CallbackQuery,
                                button: Button,
                                dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=GarageState.home)


async def garage_enter_car_name(message: Message,
                                widget: MessageInput,
                                dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get("i18n")

    if len(message.text) > CURRENT_CAR_NAME_LENGTH:
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=i18n.error.long.car.name(
                len_message=len(message.text),
                current_length=CURRENT_CAR_NAME_LENGTH
            )
        )
        return

    car_id = await create_car(message.text, message.from_user.id)
    dialog_manager.dialog_data.update(car_name=message.text,
                                      car_id=car_id,
                                      is_first_car=False)

    await dialog_manager.start(state=CarState.home,
                               data=dialog_manager.dialog_data)
