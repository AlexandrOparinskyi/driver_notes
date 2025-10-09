from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager

from bot.states import StartState

start_router = Router()


@start_router.message(CommandStart())
async def command_start(message: Message,
                        dialog_manager: DialogManager):
    await dialog_manager.start(state=StartState.start)
