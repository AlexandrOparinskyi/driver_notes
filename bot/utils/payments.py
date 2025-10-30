import random
import uuid

from aiogram import Bot
from aiogram.types import LabeledPrice
from fluentogram import TranslatorHub
from yookassa import Payment, Configuration

from config import Config, load_config
from database import PaymentTypeEnum

config: Config = load_config()
Configuration.account_id = config.you_kassa.account_id
Configuration.secret_key = config.you_kassa.secret_key


def create_payment(user_id: int,
                   current_sum: int,
                   i18n: TranslatorHub,
                   payment_type: PaymentTypeEnum) -> str:
    payment = Payment.create({
        "amount": {
            "value": f"{float(current_sum):.2f}",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"https://t.me/{config.tg_bot.bot_username}"
        },
        "capture": True,
        "description": i18n.home.support.project(),
        "metadata": {
            "user_id": user_id,
            "payment_type": payment_type.value,
        }
    }, uuid.uuid4())

    return payment.confirmation.confirmation_url


async def create_stars_payment(chat_id: int,
                               bot: Bot,
                               amount: int,
                               i18n: TranslatorHub):
    prices = [LabeledPrice(label="Звёзды", amount=amount)]

    await bot.send_invoice(
        chat_id=chat_id,
        title="Поддержка проекта ⭐",
        description=random.choice(_get_description_text(i18n)),
        currency="XTR",
        prices=prices,
        payload=f"donation_{chat_id}_{1}",
    )


def _get_description_text(i18n: TranslatorHub):
    return [
        i18n.donation.description.one(),
        i18n.donation.description.two(),
        i18n.donation.description.three(),
        i18n.donation.description.four(),
        i18n.donation.description.five(),
    ]
