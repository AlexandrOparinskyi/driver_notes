import random

from aiogram.types import User
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id
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
                                   **kwargs) -> dict[str, str]:
    return {"home_instruction_text": i18n.home.instruction.text(),
            "home_button": i18n.home.button()}
