from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row, Url, Select, Column
from aiogram_dialog.widgets.text import Format

from bot.states import HomeState
from .getters import (getter_home,
                      getter_home_write_developer,
                      getter_home_instructions,
                      getter_home_get_instruction)
from .handlers import (home_write_developer,
                       home_instructions,
                       home_get_instruction,
                       home_garage)
from ..general import (service_in_development,
                       home_button)

home_dialog = Dialog(
    Window(
        Format("{home_text}"),
        Button(text=Format("{add_record_button}"),
               id="add_record_button",
               on_click=service_in_development),
        Row(Button(text=Format("{garage_button}"),
                   id="garage_button",
                   on_click=home_garage),
            Button(text=Format("{lk_button}"),
                   id="lk_button",
                   on_click=service_in_development)),
        Row(Button(text=Format("{instructions_button}"),
                   id="instructions_button",
                   on_click=home_instructions),
            Button(text=Format("{reviews_button}"),
                   id="reviews_button",
                   on_click=service_in_development)),
        Button(text=Format("{support_project_button}"),
               id="support_project_button",
               on_click=service_in_development),
        Button(text=Format("{write_developer_button}"),
               id="write_developer_button",
               on_click=home_write_developer),
        getter=getter_home,
        state=HomeState.home
    ),
    Window(
        Format("{home_write_developer_text}"),
        Url(text=Format("{developer_button}"),
            url=Format("{developer_url}")),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_home_write_developer,
        state=HomeState.write_developer
    ),
    Window(
        Format("{home_instruction_text}"),
        Column(Select(text=Format("{item[0]}"),
                      id="instructions",
                      item_id_getter=lambda x: x[1],
                      items="buttons",
                      on_click=home_get_instruction)),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_home_instructions,
        state=HomeState.instructions
    ),
    Window(
        Format("{instruction_text}"),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=home_instructions),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_home_get_instruction,
        state=HomeState.get_instruction
    )
)
