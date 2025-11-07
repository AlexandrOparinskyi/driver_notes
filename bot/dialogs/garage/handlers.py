from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select, ManagedCheckbox

from bot.states import GarageState, CarState, CarDataState, ServiceRecordState, RefuelRecordState
from bot.utils import create_car, get_user_by_id, get_car_by_id, delete_car_by_id, create_car_documents, \
    delete_service_by_id, delete_refuel_by_id, get_service_by_id, get_refuel_by_id
from config import CURRENT_CAR_NAME_LENGTH


async def garage_add_car(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    user = await get_user_by_id(callback.from_user.id)
    if len(user.get_active_cars) >= 2 and not user.is_premium:
        await dialog_manager.switch_to(state=GarageState.offer_premium)
        return

    await dialog_manager.switch_to(state=GarageState.car_name)


async def garage_select_car(callback: CallbackQuery,
                            widget: Select,
                            dialog_manager: DialogManager,
                            item_id: str):
    dialog_manager.dialog_data.update(car_id=item_id)

    await dialog_manager.switch_to(state=GarageState.car_detail)


async def back_button_to_garage(callback: CallbackQuery,
                                button: Button,
                                dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=GarageState.home)


async def garage_enter_car_name(message: Message,
                                widget: MessageInput,
                                dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get("i18n")

    if len(message.text) > CURRENT_CAR_NAME_LENGTH:
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=i18n.error.long.car.name(
                len_message=len(message.text),
                current_length=CURRENT_CAR_NAME_LENGTH
            )
        )
        return

    car_id = await create_car(message.text, message.from_user.id)
    await create_car_documents(car_id)
    dialog_manager.dialog_data.update(car_name=message.text,
                                      car_id=car_id,
                                      is_first_car=False)

    await dialog_manager.start(state=CarState.home,
                               data=dialog_manager.dialog_data)


async def garage_car_edit_data(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)

    await dialog_manager.start(CarState.home,
                               data={"back_to_car": car.id, **car.to_dict})


async def garage_rename_car(callback: CallbackQuery,
                            button: Button,
                            dialog_manager: DialogManager):
    car_id = int(dialog_manager.dialog_data.get("car_id"))

    await dialog_manager.start(state=CarState.edit_car_name,
                               data={"car_id": car_id})


async def garage_car_documents(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    car_id = int(dialog_manager.dialog_data.get("car_id"))

    await dialog_manager.start(state=CarDataState.home,
                               data={"car_id": car_id})


async def garage_delete_car(callback: CallbackQuery,
                            button: Button,
                            dialog_manager: DialogManager):
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    await delete_car_by_id(car_id)

    await dialog_manager.switch_to(state=GarageState.home)


async def garage_get_records(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(n="page_0")

    await dialog_manager.switch_to(state=GarageState.car_records)


async def back_button_to_car_detail(callback: CallbackQuery,
                                    button: Button,
                                    dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=GarageState.car_detail)


async def garage_check_records_filter(callback: CallbackQuery,
                                      checkbox: ManagedCheckbox,
                                      dialog_manager: DialogManager):
    key = checkbox.widget.widget_id
    dialog_manager.dialog_data[key] = checkbox.is_checked()


async def garage_next_button(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    n = int(dialog_manager.dialog_data.get("n").split("_")[1])
    len_records = int(dialog_manager.dialog_data.get("len_records"))

    if n + 1 >= len_records:
        return

    dialog_manager.dialog_data.update(n=f"page_{n + 1}")


async def garage_prev_button(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    n = int(dialog_manager.dialog_data.get("n").split("_")[1])

    if n == 0:
        return

    dialog_manager.dialog_data.update(n=f"page_{n - 1}")


async def garage_select_record(callback: CallbackQuery,
                               widget: Select,
                               dialog_manager: DialogManager,
                               item_id: str):
    record, r_id = item_id.split("_")
    dialog_manager.dialog_data.update(record_type=record,
                                      record_id=r_id)

    await dialog_manager.switch_to(state=GarageState.record)


async def back_button_to_select_record(callback: CallbackQuery,
                                       button: Button,
                                       dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=GarageState.car_records)


async def garage_delete_record(callback: CallbackQuery,
                               button: Button,
                               dialog_manager: DialogManager):
    r_type = dialog_manager.dialog_data.get("record_type")
    r_id = int(dialog_manager.dialog_data.get("record_id"))

    if r_type == "service":
        await delete_service_by_id(r_id)
    if r_type == "refuel":
        await delete_refuel_by_id(r_id)

    await dialog_manager.switch_to(state=GarageState.car_records)


async def garage_edit_record(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    r_type = dialog_manager.dialog_data.get("record_type")
    r_id = int(dialog_manager.dialog_data.get("record_id"))

    if r_type == "service":
        service = await get_service_by_id(r_id)
        service_type = (service.service_type.name
                        if service.service_type else None)
        data = {"service_car": service.car_id,
                "service_title": service.title,
                "service_description": service.description,
                "service_date": service.service_date,
                "service_type": service_type,
                "service_price": service.total_price,
                "service_name": service.service_center,
                "service_edit": True}
        data.update(**dialog_manager.dialog_data)
        if service.service_parts:
            part_data = {}
            count = 0
            for i in service.service_parts:
                part_data[f"part_{count}"] = {
                    "part_name": i.name,
                    "part_price": i.total_price if i.total_price else 0,
                    "part_quantity": i.quantity,
                    "part_price_per_unit": i.price_per_unit,
                    "part_number": i.part_number,
                    "part_comment": i.comment
                }
                count += 1
            data["part_data"] = part_data
            data["selected_part"] = "part_0"
        if service.service_works:
            work_data = {}
            count = 0
            for i in service.service_works:
                work_data[f"work_{count}"] = {
                    "work_name": i.name,
                    "work_price": i.price if i.price else 0,
                    "work_description": i.description
                }
            data["work_data"] = work_data
            data["selected_work"] = "work_0"
        await dialog_manager.start(state=ServiceRecordState.home,
                                   data=data)
        return

    if r_type == "refuel":
        refuel = await get_refuel_by_id(r_id)
        r_type = refuel.fuel_type.name if refuel.fuel_type else None
        r_stat = refuel.gas_station.name if refuel.gas_station else None
        data = {"refuel_car": refuel.car_id,
                "refuel_price": refuel.total_price,
                "refuel_date": refuel.refuel_date,
                "refuel_liters": refuel.liters,
                "refuel_time": refuel.time,
                "refuel_type": r_type,
                "refuel_station": r_stat,
                "refuel_edit": True}
        data.update(**dialog_manager.dialog_data)
        await dialog_manager.start(state=RefuelRecordState.home,
                                   data=data)
        return
