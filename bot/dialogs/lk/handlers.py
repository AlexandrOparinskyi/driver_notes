from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from fluentogram import TranslatorHub

from bot.states import LkStates
from bot.utils import change_user_locale


async def lk_back_to_home(callback: CallbackQuery,
                          button: Button,
                          dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=LkStates.home)


async def lk_invite_friend(callback: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager):
    if not dialog_manager.dialog_data.get("empty_link"):
        dialog_manager.dialog_data.update(empty_link=False)

    await dialog_manager.switch_to(state=LkStates.invite_friend)


async def lk_change_link_and_text(callback: CallbackQuery,
                                  button: Button,
                                  dialog_manager: DialogManager):
    if dialog_manager.dialog_data.get("empty_link"):
        dialog_manager.dialog_data.update(empty_link=False)
    else:
        dialog_manager.dialog_data.update(empty_link=True)


async def lk_change_language_button(callback: CallbackQuery,
                                    button: Button,
                                    dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=LkStates.change_language)


async def lk_change_language(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    lang = button.widget_id.split("_")[0]
    await change_user_locale(callback.from_user.id, lang)

    hub: TranslatorHub = dialog_manager.middleware_data.get(
        "_translator_hub"
    )
    dialog_manager.middleware_data["i18n"] = hub.get_translator_by_locale(
        locale=lang
    )
