from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select
from aiogram_dialog.widgets.text import Format

from bot.states import GarageState
from .getters import (getter_garage,
                      getter_car_name,
                      getter_car_offer_premium,
                      getter_car_detail)
from .handlers import (garage_add_car,
                       back_button_to_garage,
                       garage_enter_car_name,
                       garage_select_car,
                       garage_car_edit_data, garage_rename_car)
from ..general import (home_button,
                       generale_message_not_text,
                       service_in_development)

garage_dialog = Dialog(
    Window(
        Format("{garage_text}"),
        Group(Select(text=Format("{item.name}"),
                     id="car",
                     item_id_getter=lambda x: x.id,
                     items="cars",
                     on_click=garage_select_car)),
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
    ),
    Window(
        Format("{car_detail_text}"),
        Group(Button(text=Format("{edit_name_button}"),
               id="edit_name_button",
               on_click=garage_rename_car),
        Button(text=Format("{edit_data_button}"),
               id="edit_data_button",
               on_click=garage_car_edit_data),
        Button(text=Format("{edit_documents_button}"),
               id="edit_documents_button",
               on_click=None),
        Button(text=Format("{get_report_button}"),
               id="get_report_button",
               on_click=service_in_development),
              width=2),
        Button(text=Format("{setting_notification_button}"),
               id="setting_notification_button",
               on_click=service_in_development),
        Button(text=Format("{delete_car_button}"),
               id="delete_car_button",
               on_click=None),
        Button(text=Format("{back_button}"),
               id="back_button_to_garage",
               on_click=back_button_to_garage),
        getter=getter_car_detail,
        state=GarageState.car_detail
    )
)
