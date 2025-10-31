from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def refuel_record_check_price(message: Message,
                                    dialog_manager: DialogManager) -> bool:
    i18n = dialog_manager.middleware_data.get("i18n")

    if message.text[0] == "-":
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=i18n.refuel.record.error.enter.price.text()
        )
        return False

    try:
        float(message.text.replace(",", "."))
        return True
    except ValueError:
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=i18n.refuel.record.error.enter.price.text()
        )
        return False

    return True


async def refuel_record_check_part(message: Message,
                                   dialog_manager: DialogManager) -> bool:
    i18n = dialog_manager.middleware_data.get("i18n")
    refuel_part = dialog_manager.dialog_data.get("refuel_part")

    answer_data = {
        "refuel_price": i18n.refuel.record.error.enter.price.text(),
        "refuel_liters": i18n.refuel.record.error.edit.liters.text()
    }

    if refuel_part == "refuel_time":
        return True

    if message.text[0] == "-":
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=answer_data.get(refuel_part)
        )
        return False

    try:
        float(message.text.replace(",", "."))
        return True
    except ValueError:
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=answer_data.get(refuel_part)
        )
        return False

    return True