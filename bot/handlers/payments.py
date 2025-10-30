import random

from aiogram import Router, Bot
from aiogram.enums import ContentType
from aiogram.types import (PreCheckoutQuery,
                           Message,
                           SuccessfulPayment,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
from fluentogram import TranslatorHub

payment_router = Router()


@payment_router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery,
                                     bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@payment_router.message(lambda message: message.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: Message,
                                     i18n: TranslatorHub):
    payment: SuccessfulPayment = message.successful_payment

    amount = payment.total_amount // 100
    currency = payment.currency

    thank_you_messages = [
        i18n.donation.thanks.one(amount=amount, currency=currency),
        i18n.donation.thanks.two(amount=amount, currency=currency),
        i18n.donation.thanks.three(amount=amount, currency=currency),
        i18n.donation.thanks.four(amount=amount, currency=currency),
        i18n.donation.thanks.five(amount=amount, currency=currency)
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=i18n.home.button(),
                callback_data="home_button"
            )]
        ]
    )
    await message.answer(text=random.choice(thank_you_messages),
                         reply_markup=keyboard)
