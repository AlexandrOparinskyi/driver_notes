from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def service_record_check_text(message: Message,
                                    dialog_manager: DialogManager):
    service_part = dialog_manager.dialog_data.get("service_part")
    i18n = dialog_manager.middleware_data.get("i18n")

    if service_part in ("service_description",
                        "service_name",
                        "service_title"):
        return True

    if service_part == "service_mileage":
        if not message.text.isdigit():
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.service.record.edit.mileage.error.text()
            )
            return False

    if service_part == "service_price":
        if message.text[0] == "-":
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.service.record.edit.price.error.text()
            )
            return False
        try:
            float(message.text.replace(",", "."))
            return True
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.service.record.edit.price.error.text()
            )
            return False

    return True
