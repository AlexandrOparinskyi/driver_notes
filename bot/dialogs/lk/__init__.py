from aiogram import Router

from .dialogs import lk_dialog


def register_lk_dialogs(router: Router):
    router.include_router(lk_dialog)
