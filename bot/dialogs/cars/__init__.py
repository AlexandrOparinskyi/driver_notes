from aiogram import Router

from .dialogs import edit_car_dialog


def register_car_dialogs(router: Router) -> None:
    router.include_router(edit_car_dialog)
