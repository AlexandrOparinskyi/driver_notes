import random

from aiogram import Bot
from aiogram.types import LabeledPrice
from fluentogram import TranslatorHub

from config import Config, load_config


async def create_payment(chat_id: int,
                         bot: Bot,
                         current_sum: int,
                         i18n: TranslatorHub):
    config: Config = load_config()

    donation_descriptions = [
        i18n.donation.description.one(),
        i18n.donation.description.two(),
        i18n.donation.description.three(),
        i18n.donation.description.four(),
        i18n.donation.description.five(),
    ]

    await bot.send_invoice(
        chat_id=chat_id,
        title="Поддержать проект",
        description=random.choice(donation_descriptions),
        payload=f"donation_{chat_id}",
        provider_token=config.you_kassa.token,
        currency="rub",
        prices=[
            LabeledPrice(label="Поддержка проекта", amount=int(current_sum))
        ],
        start_parameter="donation",
        request_timeout=15
    )