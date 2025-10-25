from aiogram.fsm.state import StatesGroup, State


class StartState(StatesGroup):
    start = State()
    acquaintance = State()
    car_name = State()
    completed_car_name = State()
    confirm = State()


class HomeState(StatesGroup):
    home = State()
    write_developer = State()
    instructions = State()
    get_instruction = State()
    select_record = State()


class CarState(StatesGroup):
    home = State()
    edit_part = State()
    edit_car_name = State()


class CarDataState(StatesGroup):
    home = State()
    edit_part = State()


class GarageState(StatesGroup):
    home = State()
    car_name = State()
    offer_premium = State()
    car_detail = State()
