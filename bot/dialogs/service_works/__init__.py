from aiogram import Router

from .dialogs import service_work_dialog


def register_service_work_dialogs(router: Router):
    router.include_router(service_work_dialog)
