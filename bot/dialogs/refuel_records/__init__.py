from aiogram import Router

from .dialogs import refuel_record_dialog


def register_refuel_record_dialogs(router: Router):
    router.include_router(refuel_record_dialog)
