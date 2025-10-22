from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub


async def getter_start(i18n: TranslatorHub,
                       event_from_user: User,
                       **kwargs) -> dict[str, str]:
    username = event_from_user.first_name

    return {"start_text": i18n.start.text(username=username),
            "start_acquaintance_button": i18n.start.acquaintance.button()}


async def getter_start_acquaintance(i18n: TranslatorHub,
                                    **kwargs) -> dict[str, str]:
    return {"start_acquaintance_text": i18n.start.acquaintance.text(),
            "add_car_button": i18n.start.add.car.button()}


async def getter_start_car_name(i18n: TranslatorHub,
                                **kwargs) -> dict[str, str]:
    return {"start_car_name_text": i18n.start.car.name.text()}


async def getter_completed_car_name(i18n: TranslatorHub,
                                    dialog_manager: DialogManager,
                                    **kwargs) -> dict[str, str]:
    car_name = dialog_manager.dialog_data.get("car_name")
    start_completed_car_name_text = i18n.start.completed.add.car(
        car_name=car_name,
    )

    return {"start_completed_car_name_text": start_completed_car_name_text,
            "car_menu_button": i18n.start.car.menu.button(),
            "home_button": i18n.home.button()}


async def getter_start_confirm(i18n: TranslatorHub,
                               **kwargs) -> dict[str, str]:
    return {"start_confirm_text": i18n.start.confirm.text(),
            "home_button": i18n.home.button()}