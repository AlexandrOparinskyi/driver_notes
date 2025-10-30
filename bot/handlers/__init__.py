from aiogram import Router

from .payments import payment_router, process_success_rub_payment
from .start import start_router


def register_handlers(router: Router):
    router.include_router(start_router)
    router.include_router(payment_router)


__all__ = ["process_success_rub_payment"]
