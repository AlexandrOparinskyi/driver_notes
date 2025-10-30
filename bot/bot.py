import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from bot.dialogs import register_dialogs
from bot.handlers import register_handlers
from bot.middlewares import TranslatorRunnerMiddleware

logger = logging.getLogger(__name__)


async def main(
        token: str,
        translator_hub: TranslatorHub,
        storage: RedisStorage | MemoryStorage = MemoryStorage()
) -> None:
    bot: Bot = Bot(token=token,
                   default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp: Dispatcher = Dispatcher(storage=storage)

    await bot.set_my_commands(
        commands=[
            BotCommand(
                command="home",
                description="♻️ Home"
            )
        ]
    )

    dp.update.middleware(TranslatorRunnerMiddleware())

    register_handlers(dp)
    register_dialogs(dp)
    setup_dialogs(dp)

    try:
        await dp.start_polling(bot, _translator_hub=translator_hub)
    except Exception as err:
        logger.error(f"Bot don`t started: {err}")
