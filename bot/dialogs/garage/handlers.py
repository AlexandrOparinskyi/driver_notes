from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import GarageState, CarState, CarDataState
from bot.utils import create_car, get_user_by_id, get_car_by_id, delete_car_by_id
from config import CURRENT_CAR_NAME_LENGTH


async def garage_add_car(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    user = await get_user_by_id(callback.from_user.id)
    if len(user.get_active_cars) >= 2 and not user.is_premium:
        await dialog_manager.switch_to(state=GarageState.offer_premium)
        return

    await dialog_manager.switch_to(state=GarageState.car_name)


async def garage_select_car(callback: CallbackQuery,
                            widget: Select,
                            dialog_manager: DialogManager,
                            item_id: str):
    dialog_manager.dialog_data.update(car_id=item_id)

    await dialog_manager.switch_to(state=GarageState.car_detail)


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


async def garage_car_edit_data(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)

    await dialog_manager.start(CarState.home,
                               data={"back_to_car": car.id, **car.to_dict})


async def garage_rename_car(callback: CallbackQuery,
                            button: Button,
                            dialog_manager: DialogManager):
    car_id = int(dialog_manager.dialog_data.get("car_id"))

    await dialog_manager.start(state=CarState.edit_car_name,
                               data={"car_id": car_id})


async def garage_car_documents(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    car_id = int(dialog_manager.dialog_data.get("car_id"))

    await dialog_manager.start(state=CarDataState.home,
                               data={"car_id": car_id})


async def garage_delete_car(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    await delete_car_by_id(car_id)

    await dialog_manager.switch_to(GarageState.home)
