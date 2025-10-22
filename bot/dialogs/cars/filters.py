from datetime import datetime

from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def car_check_enter_part(message: Message,
                               dialog_manager: DialogManager):
    car_part = dialog_manager.dialog_data.get("car_part")

    if car_part not in ("car_year", "car_mileage"):
        return True

    if car_part == "car_year":
        current_year = datetime.now().year

        try:
            now_year = int(message.text)
            if current_year < now_year or now_year < 1900:
                dialog_manager.show_mode = ShowMode.NO_UPDATE
                await message.answer("Not okay")
                return
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer("Not okay")
            return

    if car_part == "car_mileage":
        if not message.text.isdigit():
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer("Not okay")
            return

    return True
