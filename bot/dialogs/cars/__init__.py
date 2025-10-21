from aiogram import Router

from bot.dialogs.cars.dialogs import add_car_dialog


def register_car_dialogs(router: Router) -> None:
    router.include_routers(add_car_dialog)
