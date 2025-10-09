import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from fluentogram import TranslatorHub

logger = logging.getLogger(__name__)


async def main(
        token: str,
        translator_hub: TranslatorHub,
        storage: RedisStorage | MemoryStorage = MemoryStorage()
) -> None:
    bot: Bot = Bot(token=token)
    dp: Dispatcher = Dispatcher(storage=storage)

    try:
        await dp.start_polling(bot, _translator_hub=translator_hub)
    except Exception as err:
        logger.error(f"Bot don`t started: {err}")
