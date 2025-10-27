from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Group, Select
from aiogram_dialog.widgets.text import Format

from bot.states import ServiceRecordState
from .getters import getter_service_record_home
from .handlers import service_record_back_to_select
from ..general import service_in_development

service_record_dialog = Dialog(
    Window(
        Format("{service_record_home_text}"),
        Button(text=Format("{add_part_button}"),
               id="add_part_button",
               on_click=service_in_development),
        Button(text=Format("{add_work_button}"),
               id="add_work_button",
               on_click=service_in_development),
        Group(Select(text=Format("{item[0]}"),
                     id="select_service_record_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=None),
              width=2),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=service_record_back_to_select),
        getter=getter_service_record_home,
        state=ServiceRecordState.home
    )
)
