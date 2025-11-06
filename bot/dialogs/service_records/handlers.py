from datetime import date

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import (ServiceRecordState,
                        HomeState,
                        ServicePartState,
                        ServiceWorkState, GarageState)
from bot.utils import (create_service_record,
                       update_mileage,
                       create_service_parts,
                       create_service_works)


async def service_record_back_to_select(callback: CallbackQuery,
                                        button: Button,
                                        dialog_manager: DialogManager):
    if dialog_manager.dialog_data.get("service_edit"):
        await dialog_manager.start(state=GarageState.record,
                                   data=dialog_manager.dialog_data)
        return

    await dialog_manager.start(state=HomeState.select_record,
                               mode=StartMode.RESET_STACK)


async def service_record_edit_part(callback: CallbackQuery,
                                   widget: Select,
                                   dialog_manager: DialogManager,
                                   item_id: str):
    dialog_manager.dialog_data.update(service_part=item_id)

    if item_id in ("service_car", "service_type"):
        await dialog_manager.switch_to(state=ServiceRecordState.edit_button)
        return

    if item_id == "service_date":
        await dialog_manager.switch_to(state=ServiceRecordState.calendar)
        return

    await dialog_manager.switch_to(state=ServiceRecordState.edit_text)


async def service_record_back_to_select_part(callback: CallbackQuery,
                                             button: Button,
                                             dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=ServiceRecordState.home)


async def service_record_save_selected_part(callback: CallbackQuery,
                                            widget: Select,
                                            dialog_manager: DialogManager,
                                            item_id: str):
    service_part = dialog_manager.dialog_data.get("service_part")
    dialog_manager.dialog_data[service_part] = item_id

    await dialog_manager.switch_to(state=ServiceRecordState.home)


async def service_record_save_enter_part(message: Message,
                                         widget: MessageInput,
                                         dialog_manager: DialogManager):
    service_part = dialog_manager.dialog_data.get("service_part")
    m_text = message.text

    if service_part == "service_price":
        m_text = m_text.replace(",", ".")

    dialog_manager.dialog_data[service_part] = m_text

    await dialog_manager.switch_to(state=ServiceRecordState.home)


async def service_record_save_select_date(callback: CallbackQuery,
                                          widget,
                                          dialog_manager: DialogManager,
                                          c_date: date):
    service_part = dialog_manager.dialog_data.get("service_part")
    dialog_manager.dialog_data[service_part] = c_date

    await dialog_manager.switch_to(state=ServiceRecordState.home)


async def service_record_save_button(callback: CallbackQuery,
                                     button: Button,
                                     dialog_manager: DialogManager):
    if dialog_manager.dialog_data.get("service_edit"):
        # Добавить сохранение сервиса + работ и запчастей
        await dialog_manager.start(state=GarageState.record,
                                   data=dialog_manager.dialog_data)
        return

    i18n = dialog_manager.middleware_data.get("i18n")
    service_id = await create_service_record(user_id=callback.from_user.id,
                                             **dialog_manager.dialog_data)


    mileage = dialog_manager.dialog_data.get("service_mileage")
    if mileage:
        car_id = int(dialog_manager.dialog_data.get("service_car"))
        await update_mileage(car_id, int(mileage))

    service_part_data = dialog_manager.dialog_data.get("part_data")
    if service_part_data:
        for value in service_part_data.values():
            await create_service_parts(service_id, value)

    service_work_data = dialog_manager.dialog_data.get("work_data")
    if service_work_data:
        for value in service_work_data.values():
            await create_service_works(service_id, value)

    await callback.answer(
        text=i18n.service.record.success.added.text()
    )
    await dialog_manager.start(state=HomeState.home)


async def service_record_add_part(callback: CallbackQuery,
                                  button: Button,
                                  dialog_manager: DialogManager):
    if dialog_manager.dialog_data.get("part_data"):
        await dialog_manager.start(state=ServicePartState.home,
                                       data=dialog_manager.dialog_data)
        return

    await dialog_manager.start(state=ServicePartState.enter_name,
                               data=dialog_manager.dialog_data)


async def service_record_add_work(callback: CallbackQuery,
                                  button: Button,
                                  dialog_manager: DialogManager):
    if dialog_manager.dialog_data.get("work_data"):
        await dialog_manager.start(state=ServiceWorkState.home,
                                       data=dialog_manager.dialog_data)
        return

    await dialog_manager.start(state=ServiceWorkState.enter_name,
                               data=dialog_manager.dialog_data)
