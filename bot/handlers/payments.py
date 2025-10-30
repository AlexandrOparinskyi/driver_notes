import random

from aiogram import Router, Bot
from aiogram.enums import ContentType
from aiogram.types import (PreCheckoutQuery,
                           Message,
                           SuccessfulPayment,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id

payment_router = Router()


@payment_router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery,
                                     bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@payment_router.message(
    lambda message: message.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def process_success_stars_payment(message: Message,
                                        i18n: TranslatorHub):
    payment: SuccessfulPayment = message.successful_payment

    currency = "⭐"
    amount = payment.total_amount

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


async def process_success_rub_payment(bot: Bot,
                                      user_id: int,
                                      amount: str,
                                      currency: str):
    user = await get_user_by_id(user_id)
    lang_code = user.locale.value

    message_data = {
        "ru": (f"🙏 Благодарим за ваше пожертвование!\n\nСумма: {amount} "
               f"{currency}\n\nВаша поддержка помогает нам развиваться и стан"
               f"овиться лучше! \n\nИскренне благодарим за доверие и помощь!"),
        "en": (f"🙏 Thank you for your generous donation!\n\nAmount: {amount} "
               f"{currency}\n\nYour contribution makes a real difference"
               f" and helps us continue our work.\n\nWe are truly "
               f"grateful for your support!")
    }
    button_data = {
        "ru": "♻️ В главное меню",
        "en": "♻️ To Main Menu"
    }
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=button_data[lang_code],
                callback_data="home_button"
            )]
        ]
    )

    await bot.send_message(
        chat_id=user_id,
        text=message_data[lang_code],
        reply_markup=keyboard,
    )