from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def service_work_check_text(message: Message,
                                  dialog_manager: DialogManager):
    work_param = dialog_manager.dialog_data.get("work_param")
    i18n = dialog_manager.middleware_data.get("i18n")

    if work_param == "work_price":
        if message.text[0] == "-":
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.service.work.edit.price.error.text()
            )
            return False
        try:
            float(message.text.replace(",", "."))
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.service.work.edit.price.error.text()
            )
            return False

    return True
