from aiogram import Router

from .dialogs import service_record_dialog


def register_service_record_dialogs(router: Router):
    router.include_router(service_record_dialog)
