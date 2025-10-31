from datetime import datetime, date

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select, ManagedCheckbox

from bot.states import HomeState, RefuelRecordState
from bot.utils import get_user_by_id, get_car_by_id, create_refuel_record
from database import EngineTypeEnum, FuelTypeEnum

FUEL_TYPE_DATA = {
    EngineTypeEnum.DIESEL: FuelTypeEnum.DIESEL.name,
    EngineTypeEnum.PETROL: FuelTypeEnum.PETROL_95.name,
    EngineTypeEnum.GAS: FuelTypeEnum.GAS.name
}


async def refuel_record_back_to_select_record(callback: CallbackQuery,
                                              button: Button,
                                              dialog_manager: DialogManager):
    await dialog_manager.start(state=HomeState.select_record)


async def refuel_record_enter_price(message: Message,
                                    widget: MessageInput,
                                    dialog_manager: DialogManager):
    user = await get_user_by_id(message.from_user.id)
    car = user.get_main_car

    if car.engine_type in FUEL_TYPE_DATA.keys():
        dialog_manager.dialog_data.update(
            refuel_type=FUEL_TYPE_DATA.get(car.engine_type)
        )

    dialog_manager.dialog_data.update(
        refuel_price=message.text.replace(",", "."),
        refuel_car=car.id,
        refuel_date=datetime.now()
    )

    await dialog_manager.switch_to(state=RefuelRecordState.home)


async def refuel_record_edit_param(callback: CallbackQuery,
                                   widget: Select,
                                   dialog_manager: DialogManager,
                                   item_id: str):
    dialog_manager.dialog_data.update(refuel_part=item_id)

    if item_id == "refuel_date":
        await dialog_manager.switch_to(state=RefuelRecordState.calendar)
        return

    if item_id in ("refuel_car", "refuel_station", "refuel_type"):
        await dialog_manager.switch_to(state=RefuelRecordState.edit_button)
        return

    await dialog_manager.switch_to(state=RefuelRecordState.edit_text)


async def refuel_record_full_tank_checkbox(callback: CallbackQuery,
                                           checkbox: ManagedCheckbox,
                                           dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(full_tank=checkbox.is_checked())


async def refuel_record_back_to_home(callback: CallbackQuery,
                                     button: Button,
                                     dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=RefuelRecordState.home)


async def refuel_record_edit_date(callback: CallbackQuery,
                                  widget,
                                  dialog_manager: DialogManager,
                                  selected_date: date):
    dialog_manager.dialog_data.update(refuel_date=selected_date)

    await dialog_manager.switch_to(state=RefuelRecordState.home)


async def refuel_record_edit_part(callback: CallbackQuery,
                                  widget: Select,
                                  dialog_manager: DialogManager,
                                  item_id: str):
    refuel_part = dialog_manager.dialog_data.get("refuel_part")
    dialog_manager.dialog_data[refuel_part] = item_id

    if refuel_part == "refuel_car":
        car = await get_car_by_id(int(item_id))
        if car.engine_type and car.engine_type in FUEL_TYPE_DATA.keys():
            dialog_manager.dialog_data.update(
                refuel_type=FUEL_TYPE_DATA.get(car.engine_type)
            )

    await dialog_manager.switch_to(state=RefuelRecordState.home)


async def refuel_record_enter_part(message: Message,
                                   widget: MessageInput,
                                   dialog_manager: DialogManager):
    refuel_part = dialog_manager.dialog_data.get("refuel_part")
    m_text = message.text

    if refuel_part in ("refuel_price", "refuel_liters"):
        m_text = m_text.replace(",", ".")

    dialog_manager.dialog_data[refuel_part] = m_text

    await dialog_manager.switch_to(state=RefuelRecordState.home)


async def refuel_record_save(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    await create_refuel_record(**dialog_manager.dialog_data)

    i18n = dialog_manager.middleware_data.get("i18n")

    await callback.answer(
        text=i18n.refuel.record.success.added.text()
    )
    await dialog_manager.start(state=HomeState.home)
