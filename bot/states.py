from aiogram.fsm.state import StatesGroup, State


class StartState(StatesGroup):
    start = State()
    acquaintance = State()
    car_name = State()
    completed_car_name = State()


class HomeState(StatesGroup):
    home = State()
