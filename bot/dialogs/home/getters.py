import random

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id, get_instruction_by_locale, get_instruction_by_id
from config import Config, load_config


async def getter_home(i18n: TranslatorHub,
                      event_from_user: User,
                      **kwargs) -> dict[str, str]:
    phrases = [i18n.home.motivation.phrase.one(),
               i18n.home.motivation.phrase.two(),
               i18n.home.motivation.phrase.three(),
               i18n.home.motivation.phrase.four(),
               i18n.home.motivation.phrase.five(),
               i18n.home.motivation.phrase.six()]
    user = await get_user_by_id(event_from_user.id)

    return {"home_text": i18n.home.text(username=user.first_name,
                                        motivation=random.choice(phrases),
                                        car_count=len(user.get_active_cars)),
            "add_record_button": i18n.add.record.button(),
            "garage_button": i18n.garage.button(),
            "lk_button": i18n.lk.button(),
            "instructions_button": i18n.instructions.button(),
            "reviews_button": i18n.reviews.button(),
            "support_project_button": i18n.support.project.button(),
            "write_developer_button": i18n.write.developer.button()}


async def getter_home_write_developer(i18n: TranslatorHub,
                                      **kwargs) -> dict[str, str]:
    config: Config = load_config()

    return {"home_write_developer_text": i18n.home.write.developer.text(),
            "home_button": i18n.home.button(),
            "developer_button": i18n.developer.button(),
            "developer_url": f"https://t.me/{config.tg_bot.dev_url}"}


async def getter_home_instructions(i18n: TranslatorHub,
                                   event_from_user: User,
                                   **kwargs) -> dict[str, str | list]:
    instr = await get_instruction_by_locale(event_from_user.language_code)
    buttons = [(i.title, i.id) for i in instr]

    return {"home_instruction_text": i18n.home.instruction.text(),
            "home_button": i18n.home.button(),
            "buttons": buttons}


async def getter_home_get_instruction(i18n: TranslatorHub,
                                      dialog_manager: DialogManager,
                                      **kwargs) -> dict[str, str]:
    instr_id = int(dialog_manager.dialog_data.get("instr_id"))
    instruction = await get_instruction_by_id(instr_id)

    return {"instruction_text": instruction.text,
            "home_button": i18n.home.button(),
            "back_button": i18n.back.button()}


async def getter_home_select_record(i18n: TranslatorHub,
                                    **kwargs) -> dict[str, str]:
    return {"select_record_text": i18n.home.select.record.text(),
            "refuel_button": i18n.home.refuel.button(),
            "service_button": i18n.home.service.button(),
            "purchase_button": i18n.home.purchase.button(),
            "service_other_button": i18n.home.other.button(),
            "home_button": i18n.home.button()}


async def getter_home_donate(i18n: TranslatorHub,
                             **kwargs) -> dict[str, str | list]:
    price_buttons = [(100, 10000), (200, 20000), (500, 50000),
                     (1000, 100000), (2000, 200000), (5000, 500000)]

    return {"donate_text": i18n.home.donate.text(),
            "home_button": i18n.home.button(),
            "price_buttons": price_buttons,
            "home_donate_start_button": i18n.home.donate.stars.button()}


async def getter_home_donate_start(i18n: TranslatorHub,
                                   **kwargs) -> dict[str, str | list]:
    stars_button = [(5, 5), (10, 10), (20, 20),
                    (50, 50), (100, 100), (500, 500)]

    return {"donate_text": i18n.home.donate.text(),
            "home_button": i18n.home.button(),
            "stars_button": stars_button,
            "home_donate_rubles_button": i18n.home.donate.rubles.button()}