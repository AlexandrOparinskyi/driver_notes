import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id
from database import User as DbUser

logger = logging.getLogger(__name__)


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user: User = data.get('event_from_user')
        db_user: DbUser = await get_user_by_id(user.id)
        hub: TranslatorHub = data.get('_translator_hub')

        if user is None:
            return await handler(event, data)

        if db_user is None:
            data['i18n'] = hub.get_translator_by_locale(
                locale=user.language_code
            )
        else:
            data['i18n'] = hub.get_translator_by_locale(
                locale=db_user.locale.value
            )

        return await handler(event, data)
