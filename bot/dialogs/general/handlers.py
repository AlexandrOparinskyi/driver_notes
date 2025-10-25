from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.states import HomeState


async def generale_message_not_text(message: Message,
                                    widget: MessageInput,
                                    dialog_manager: DialogManager):
    dialog_manager.show_mode = ShowMode.NO_UPDATE
    i18n = dialog_manager.middleware_data.get("i18n")

    await message.answer(
        text=i18n.general.message.no.text()
    )


async def home_button(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    await dialog_manager.start(state=HomeState.home,
                               mode=StartMode.RESET_STACK)


async def service_in_development(callback: CallbackQuery,
                                 button: Button,
                                 dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get("i18n")
    dialog_manager.show_mode = ShowMode.NO_UPDATE

    await callback.answer(text=i18n.service.developing.text(),
                          show_alert=True)
