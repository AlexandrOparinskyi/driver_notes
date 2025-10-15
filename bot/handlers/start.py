from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager

from bot.states import StartState, HomeState
from bot.utils import get_user_by_id, create_user

start_router = Router()


@start_router.message(Command(commands=["start", "home"]))
async def command_start(message: Message,
                        dialog_manager: DialogManager):
    user = await get_user_by_id(message.from_user.id)

    if user is None:
        await create_user(message.from_user.id,
                          message.from_user.username,
                          message.from_user.first_name,
                          message.from_user.last_name)
        await dialog_manager.start(state=StartState.start)
        return

    await dialog_manager.start(state=StartState.start)
