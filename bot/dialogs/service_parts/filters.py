from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def service_part_check_text(message: Message,
                                  dialog_manager: DialogManager):
    part_param = dialog_manager.dialog_data.get("part_param")
    i18n = dialog_manager.middleware_data.get("i18n")

    if part_param in ("part_number", "part_name", "part_comment"):
        return True

    if (part_param == "part_quantity" and
            not message.text.isdigit() and
            message.text[0] == "-"):
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=i18n.service.part.edit.quantity.error.text()
        )
        return False

    if part_param in ("part_price", "part_price_per_unit"):
        if message.text[0] == "-":
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.service.part.edit.price.error.text()
            )
            return False
        try:
            float(message.text.replace(",", "."))
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.service.part.edit.price.error.text()
            )
            return False

    return True
