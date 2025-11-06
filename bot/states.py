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
    donate = State()
    donate_stars = State()
    get_link = State()
    not_car = State()


class CarState(StatesGroup):
    home = State()
    edit_part = State()
    edit_car_name = State()


class CarDataState(StatesGroup):
    home = State()
    edit_documents = State()
    calendar = State()


class GarageState(StatesGroup):
    home = State()
    car_name = State()
    offer_premium = State()
    car_detail = State()
    car_records = State()
    record = State()


class ServiceRecordState(StatesGroup):
    home = State()
    edit_button = State()
    edit_text = State()
    calendar = State()


class ServicePartState(StatesGroup):
    enter_name = State()
    home = State()
    edit_param = State()


class ServiceWorkState(StatesGroup):
    enter_name = State()
    home = State()
    edit_param = State()


class RefuelRecordState(StatesGroup):
    enter_price = State()
    home = State()
    edit_button = State()
    edit_text = State()
    calendar = State()


class LkStates(StatesGroup):
    home = State()
    invite_friend = State()
    change_language = State()
