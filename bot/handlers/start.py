from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, StartMode

from bot.states import StartState, HomeState
from bot.utils import get_user_by_id, create_user, add_bonus_points_user

start_router = Router()


@start_router.message(Command(commands=["start", "home"]))
async def command_start(message: Message,
                        command: CommandObject,
                        dialog_manager: DialogManager):
    ref_code = command.args
    user = await get_user_by_id(message.from_user.id)

    if user is None:
        if ref_code:
            await create_user(message.from_user.id,
                              message.from_user.username,
                              message.from_user.first_name,
                              message.from_user.last_name,
                              message.from_user.language_code)
            await add_bonus_points_user(message.from_user.id, 100)
        else:
            await create_user(message.from_user.id,
                              message.from_user.username,
                              message.from_user.first_name,
                              message.from_user.last_name,
                              message.from_user.language_code)

        if ref_code and message.from_user.id != int(ref_code):
            await add_bonus_points_user(int(ref_code), 50)

        await dialog_manager.start(state=StartState.start,
                                   mode=StartMode.RESET_STACK)
        return

    await dialog_manager.start(state=HomeState.home,
                               mode=StartMode.RESET_STACK)


@start_router.callback_query(F.data == "home_button")
async def command_home_cb(callback: CallbackQuery,
                          dialog_manager: DialogManager):
    await dialog_manager.start(state=HomeState.home,
                               mode=StartMode.RESET_STACK)
