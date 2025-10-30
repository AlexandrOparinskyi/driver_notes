from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Format

from bot.states import LkStates
from .getters import (getter_lk_home,
                      getter_lk_invite_friend,
                      getter_lg_change_language)
from .handlers import (lk_back_to_home,
                       lk_invite_friend,
                       lk_change_link_and_text,
                       lk_change_language_button,
                       lk_change_language)
from ..general import (home_button,
                       service_in_development)

lk_dialog = Dialog(
    Window(
        Format("{lk_home_text}"),
        Button(text=Format("{connect_premium_button}"),
               id="connect_premium_button",
               on_click=service_in_development),
        Button(text=Format("{export_button}"),
               id="export_button",
               on_click=service_in_development),
        Row(Button(text=Format("{add_friend_button}"),
                   id="add_friend_button",
                   on_click=lk_invite_friend),
            Button(text=Format("{change_language_button}"),
                   id="change_language_button",
                   on_click=lk_change_language_button)),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_lk_home,
        state=LkStates.home
    ),
    Window(
        Format("{invite_friend_text}"),
        Button(text=Format("{button}"),
               id="change_link_and_text",
               on_click=lk_change_link_and_text),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=lk_back_to_home),
        getter=getter_lk_invite_friend,
        state=LkStates.invite_friend
    ),
    Window(
        Format("{change_language_text}"),
        Row(Button(text=Format("{ru_button}"),
                   id="ru_button",
                   on_click=lk_change_language),
            Button(text=Format("{en_button}"),
                   id="en_button",
                   on_click=lk_change_language)
            ),
        Button(text=Format("{back_button}"),
               id="back_button",
               on_click=lk_back_to_home),
        getter=getter_lg_change_language,
        state=LkStates.change_language
    )
)
