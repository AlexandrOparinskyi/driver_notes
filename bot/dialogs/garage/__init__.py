from aiogram import Router
from .dialogs import garage_dialog


def register_garage_dialogs(router: Router):
    router.include_routers(garage_dialog)
