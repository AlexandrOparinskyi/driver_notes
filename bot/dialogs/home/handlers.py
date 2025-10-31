from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import HomeState, GarageState, ServiceRecordState, LkStates, RefuelRecordState
from bot.utils import create_payment, create_stars_payment
from database import PaymentTypeEnum


async def home_write_developer(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=HomeState.write_developer)


async def home_instructions(callback: CallbackQuery,
                            button: Button,
                            dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=HomeState.instructions)


async def home_get_instruction(callback: CallbackQuery,
                               widget: Select,
                               dialog_manager: DialogManager,
                               item_id: str):
    dialog_manager.dialog_data.update(instr_id=item_id)

    await dialog_manager.switch_to(state=HomeState.get_instruction)


async def home_garage(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    await dialog_manager.start(state=GarageState.home)


async def home_add_param(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    await dialog_manager.start(state=HomeState.select_record)


async def home_service_record(callback: CallbackQuery,
                              button: Button,
                              dialog_manager: DialogManager):
    await dialog_manager.start(state=ServiceRecordState.home)


async def home_refuel_record(callback: CallbackQuery,
                              button: Button,
                              dialog_manager: DialogManager):
    await dialog_manager.start(state=RefuelRecordState.enter_price)


async def home_lk(callback: CallbackQuery,
                  button: Button,
                  dialog_manager: DialogManager):
    await dialog_manager.start(state=LkStates.home)


async def home_donate(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=HomeState.donate)


async def home_donate_start(callback: CallbackQuery,
                            button: Button,
                            dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=HomeState.donate_stars)


async def create_donate_payments_btn(callback: CallbackQuery,
                                     widget: Select,
                                     dialog_manager: DialogManager,
                                     item_id: str):
    link = create_payment(callback.from_user.id,
                          int(item_id),
                          dialog_manager.middleware_data.get("i18n"),
                          PaymentTypeEnum.DONATE)

    dialog_manager.dialog_data.update(payment_link=link,
                                      amount=item_id)
    await dialog_manager.switch_to(state=HomeState.get_link)


async def create_donate_payments_stars_btn(callback: CallbackQuery,
                                           widget: Select,
                                           dialog_manager: DialogManager,
                                           item_id: str):
    await create_stars_payment(callback.from_user.id,
                               dialog_manager.middleware_data.get("bot"),
                               int(item_id),
                               dialog_manager.middleware_data.get("i18n"))


async def create_donate_payments_msg(message: Message,
                                     widget: MessageInput,
                                     dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get("i18n")
    dialog_manager.show_mode = ShowMode.NO_UPDATE

    if not message.text.isdigit():
        await message.answer(
            text=i18n.donation.error.no.amount()
        )
        return

    if int(message.text) < 100:
        await message.answer(
            text=i18n.donation.error.below.minimum(amount=message.text)
        )
        return

    link = create_payment(message.from_user.id,
                          int(message.text),
                          i18n,
                          PaymentTypeEnum.DONATE)

    dialog_manager.dialog_data.update(payment_link=link,
                                      amount=message.text)
    await dialog_manager.switch_to(state=HomeState.get_link)


async def create_donate_payments_start_msg(message: Message,
                                           widget: MessageInput,
                                           dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get("i18n")
    dialog_manager.show_mode = ShowMode.NO_UPDATE

    if not message.text.isdigit():
        await message.answer(
            text=i18n.donation.error.no.amount()
        )
        return

    await create_stars_payment(message.from_user.id,
                               dialog_manager.middleware_data.get("bot"),
                               int(message.text),
                               i18n)
