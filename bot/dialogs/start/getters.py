from aiogram.types import User
from fluentogram import TranslatorHub


async def getter_start(i18n: TranslatorHub,
                       event_from_user: User,
                       **kwargs) -> dict[str, str]:
    username = event_from_user.first_name

    return {"start_text": i18n.start.text(username=username),
            "start_acquaintance_button": i18n.start.acquaintance.button()}
