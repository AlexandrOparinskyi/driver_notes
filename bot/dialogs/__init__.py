from aiogram import Router

from .cars import register_car_dialogs
from .garage import register_garage_dialogs
from .home import register_home_dialogs
from .start import register_start_dialogs


def register_dialogs(router: Router):
    register_start_dialogs(router)
    register_home_dialogs(router)
    register_car_dialogs(router)
    register_garage_dialogs(router)
