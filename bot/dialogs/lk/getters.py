from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id
from config import Config, load_config


async def getter_lk_home(i18n: TranslatorHub,
                         event_from_user: User,
                         **kwargs) -> dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    status = (i18n.lk.premium.status.text() if user.is_premium
              else i18n.lk.simple.status.text())

    lk_home_text = i18n.lk.home.text(username=user.first_name,
                                     user_status=status,
                                     bonus_points=user.bonus_points)

    return {"lk_home_text": lk_home_text,
            "home_button": i18n.home.button(),
            "connect_premium_button": i18n.lk.connect.premium.button(),
            "add_friend_button": i18n.lk.add.friend.button(),
            "change_language_button": i18n.lk.change.language.button(),
            "export_button": i18n.lk.export.button()}


async def getter_lk_invite_friend(i18n: TranslatorHub,
                                  event_from_user: User,
                                  dialog_manager: DialogManager,
                                  **kwargs) -> dict[str, str]:
    config: Config = load_config()
    empty_link = dialog_manager.dialog_data.get("empty_link")
    link = (f"https://t.me/{config.tg_bot.bot_username}"
            f"?start={event_from_user.id}")
    text_link = f"<a href='{link}'>АвтоДневник</a>"

    if empty_link:
        invite_friend_text = f"<code>{link}</code>"
        button = i18n.lk.copy.text.link.button()
    else:
        invite_friend_text = i18n.lk.invite.friend.text(
            text_link=text_link
        )
        button = i18n.lk.copy.link.button()

    return {"invite_friend_text": invite_friend_text,
            "button": button,
            "back_button": i18n.back.button()}


async def getter_lg_change_language(i18n: TranslatorHub,
                                    dialog_manager: DialogManager,
                                    **kwargs) -> dict[str, str]:
    return {"change_language_text": i18n.lk.change.language.text(),
            "ru_button": i18n.lk.change.language.ru.button(),
            "en_button": i18n.lk.change.language.en.button(),
            "back_button": i18n.back.button()}
