import random

from aiogram import Bot
from aiogram.types import LabeledPrice
from fluentogram import TranslatorHub

from config import Config, load_config

config: Config = load_config()


def get_description_text(i18n: TranslatorHub):
    return [
        i18n.donation.description.one(),
        i18n.donation.description.two(),
        i18n.donation.description.three(),
        i18n.donation.description.four(),
        i18n.donation.description.five(),
    ]


async def create_payment(chat_id: int,
                         bot: Bot,
                         current_sum: int,
                         i18n: TranslatorHub):
    await bot.send_invoice(
        chat_id=chat_id,
        title="Поддержать проект",
        description=random.choice(get_description_text(i18n)),
        payload=f"donation_{chat_id}",
        provider_token=config.you_kassa.token,
        currency="rub",
        prices=[
            LabeledPrice(label="Поддержка проекта", amount=int(current_sum))
        ],
        start_parameter="donation",
        request_timeout=15
    )


async def create_stars_payment(chat_id: int,
                               bot: Bot,
                               amount: int,
                               i18n: TranslatorHub):
    """Отправка инвойса для оплаты звездами"""

    prices = [LabeledPrice(label="Звёзды", amount=amount)]

    await bot.send_invoice(
        chat_id=chat_id,
        title="Поддержка проекта ⭐",
        description=random.choice(get_description_text(i18n)),
        currency="XTR",
        prices=prices,
        payload=f"donation_{chat_id}_{1}",
    )
