from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import ServiceRecordState, ServiceWorkState


async def service_work_back_to_record(callback: CallbackQuery,
                                      button: Button,
                                      dialog_manager: DialogManager):
    await dialog_manager.start(state=ServiceRecordState.home,
                               data=dialog_manager.dialog_data)


async def service_work_enter_name(message: Message,
                                  widget: MessageInput,
                                  dialog_manager: DialogManager):
    work_data = dialog_manager.dialog_data.get("work_data", {})
    selected_work = f"work_{len(work_data)}"
    work_data[selected_work] = {"work_name": message.text}
    dialog_manager.dialog_data.update(work_data=work_data,
                                      selected_work=selected_work)

    await dialog_manager.switch_to(state=ServiceWorkState.home)


async def service_work_select_param(callback: CallbackQuery,
                                    widget: Select,
                                    dialog_manager: DialogManager,
                                    item_id: str):
    dialog_manager.dialog_data.update(work_param=item_id)

    await dialog_manager.switch_to(state=ServiceWorkState.edit_param)


async def service_work_back_to_home(callback: CallbackQuery,
                                    button: Button,
                                    dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=ServiceWorkState.home)


async def service_work_enter_param(message: Message,
                                   widget: MessageInput,
                                   dialog_manager: DialogManager):
    work_param = dialog_manager.dialog_data.get("work_param")
    selected_work = dialog_manager.dialog_data.get("selected_work")
    work_data = dialog_manager.dialog_data.get("work_data")
    m_text = message.text

    if work_param == "work_price":
        m_text = m_text.replace(",", ".")

    work_data[selected_work][work_param] = m_text

    await dialog_manager.switch_to(state=ServiceWorkState.home)


async def service_work_next_button(callback: CallbackQuery,
                                   button: Button,
                                   dialog_manager: DialogManager):
    selected_work = dialog_manager.dialog_data.get("selected_work")
    num_selected_work = int(selected_work.split("_")[1])
    work_data = dialog_manager.dialog_data.get("work_data")

    if num_selected_work + 1 >= len(work_data):
        return

    dialog_manager.dialog_data.update(
        selected_work=f"work_{num_selected_work + 1}"
    )


async def service_work_prev_button(callback: CallbackQuery,
                                   button: Button,
                                   dialog_manager: DialogManager):
    selected_work = dialog_manager.dialog_data.get("selected_work")
    num_selected_work = int(selected_work.split("_")[1])

    if num_selected_work == 0:
        return

    dialog_manager.dialog_data.update(
        selected_work=f"work_{num_selected_work - 1}"
    )


async def service_work_delete_button(callback: CallbackQuery,
                                     button: Button,
                                     dialog_manager: DialogManager):
    selected_work = dialog_manager.dialog_data.get("selected_work")
    num_selected_work = int(selected_work.split("_")[1])
    work_data = dialog_manager.dialog_data.get("work_data")

    work_data.pop(selected_work)

    if len(work_data) == 0:
        await dialog_manager.start(state=ServiceRecordState.home)
        return

    if num_selected_work == len(work_data):
        dialog_manager.dialog_data.update(
            selected_work=f"work_{num_selected_work - 1}"
        )
    else:
        new_part_data = {}
        for i, value in enumerate(work_data.values()):
            new_part_data[f"work_{i}"] = value

        dialog_manager.dialog_data.update(work_data=new_part_data)


async def service_work_add_work_button(callback: CallbackQuery,
                                       button: Button,
                                       dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=ServiceWorkState.enter_name)
