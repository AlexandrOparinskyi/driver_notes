from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import ServiceRecordState, ServicePartState


async def service_part_back_to_record(callback: CallbackQuery,
                                      button: Button,
                                      dialog_manager: DialogManager):
    await dialog_manager.start(state=ServiceRecordState.home,
                               data=dialog_manager.dialog_data)


async def service_part_enter_name(message: Message,
                                  widget: MessageInput,
                                  dialog_manager: DialogManager):
    part_data = dialog_manager.dialog_data.get("part_data", {})
    selected_part = f"part_{len(part_data)}"
    part_data[selected_part] = {"part_name": message.text}
    dialog_manager.dialog_data.update(part_data=part_data,
                                      selected_part=selected_part)

    await dialog_manager.switch_to(state=ServicePartState.home)


async def service_part_select_param(callback: CallbackQuery,
                                    widget: Select,
                                    dialog_manager: DialogManager,
                                    item_id: str):
    dialog_manager.dialog_data.update(part_param=item_id)

    await dialog_manager.switch_to(state=ServicePartState.edit_param)


async def service_part_back_to_home(callback: CallbackQuery,
                                    button: Button,
                                    dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=ServicePartState.home)


async def service_part_enter_param(message: Message,
                                   widget: MessageInput,
                                   dialog_manager: DialogManager):
    part_param = dialog_manager.dialog_data.get("part_param")
    selected_part = dialog_manager.dialog_data.get("selected_part")
    part_data = dialog_manager.dialog_data.get("part_data")
    m_text = message.text

    if part_param in ("part_quantity", "part_price_per_unit", "part_price"):
        m_text = m_text.replace(",", ".")

    part_data[selected_part][part_param] = m_text

    await dialog_manager.switch_to(state=ServicePartState.home)


async def service_part_next_button(callback: CallbackQuery,
                                   button: Button,
                                   dialog_manager: DialogManager):
    selected_part = dialog_manager.dialog_data.get("selected_part")
    num_selected_part = int(selected_part.split("_")[1])
    part_data = dialog_manager.dialog_data.get("part_data")

    if num_selected_part + 1 >= len(part_data):
        return

    dialog_manager.dialog_data.update(
        selected_part=f"part_{num_selected_part + 1}"
    )


async def service_part_prev_button(callback: CallbackQuery,
                                   button: Button,
                                   dialog_manager: DialogManager):
    selected_part = dialog_manager.dialog_data.get("selected_part")
    num_selected_part = int(selected_part.split("_")[1])

    if num_selected_part == 0:
        return

    dialog_manager.dialog_data.update(
        selected_part=f"part_{num_selected_part - 1}"
    )


async def service_part_delete_button(callback: CallbackQuery,
                                     button: Button,
                                     dialog_manager: DialogManager):
    selected_part = dialog_manager.dialog_data.get("selected_part")
    num_selected_part = int(selected_part.split("_")[1])
    part_data = dialog_manager.dialog_data.get("part_data")

    part_data.pop(selected_part)

    if len(part_data) == 0:
        await dialog_manager.start(state=ServiceRecordState.home)
        return

    if num_selected_part == len(part_data):
        dialog_manager.dialog_data.update(
            selected_part=f"part_{num_selected_part - 1}"
        )
    else:
        new_part_data = {}
        for i, value in enumerate(part_data.values()):
            new_part_data[f"part_{i}"] = value

        dialog_manager.dialog_data.update(part_data=new_part_data)


async def service_part_add_part_button(callback: CallbackQuery,
                                       button: Button,
                                       dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=ServicePartState.enter_name)
