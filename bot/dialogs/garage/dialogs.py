from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select
from aiogram_dialog.widgets.text import Format

from bot.states import GarageState
from .getters import (getter_garage,
                      getter_car_name,
                      getter_car_offer_premium)
from .handlers import (garage_add_car,
                       back_button_to_garage,
                       garage_enter_car_name)
from ..general import (home_button,
                       generale_message_not_text,
                       service_in_development)

garage_dialog = Dialog(
    Window(
        Format("{garage_text}"),
        Group(Select(text=Format("{item.name}"),
                     id="car",
                     item_id_getter=lambda x: x.id,
                     items="cars")),
        Button(text=Format("{add_car_button}"),
               id="add_car_button",
               on_click=garage_add_car),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_garage,
        state=GarageState.home
    ),
    Window(
        Format("{car_name_text}"),
        MessageInput(func=garage_enter_car_name,
                     content_types=ContentType.TEXT),
        MessageInput(func=generale_message_not_text),
        Button(text=Format("{back_button}"),
               id="back_button_to_garage",
               on_click=back_button_to_garage),
        getter=getter_car_name,
        state=GarageState.car_name
    ),
    Window(
        Format("{car_offer_premium_text}"),
        Button(text=Format("{connect_premium_button}"),
               id="connect_premium_button",
               on_click=service_in_development),
        Button(text=Format("{back_button}"),
               id="back_button_to_garage",
               on_click=back_button_to_garage),
        Button(text=Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_car_offer_premium,
        state=GarageState.offer_premium
    )
)
