from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.states import StartState
from config import CURRENT_CAR_NAME_LENGTH


async def start_acquaintance_button(callback: CallbackQuery,
                                    button: Button,
                                    dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=StartState.acquaintance)


async def start_add_car_button(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=StartState.car_name)


async def start_enter_car_name(message: Message,
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

    # save car and returning car_id
    dialog_manager.dialog_data.update(car_name=message.text,
                                      car_id=None,
                                      is_first_car=True)

    await dialog_manager.switch_to(state=StartState.completed_car_name)
