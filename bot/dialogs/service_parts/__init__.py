from aiogram import Router

from .dialogs import service_part_dialog


def register_service_part_dialogs(router: Router):
    router.include_router(service_part_dialog)
