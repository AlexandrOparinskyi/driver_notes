from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from fastapi import APIRouter, Request

from bot.handlers import process_success_rub_payment
from bot.utils import get_payment_by_id, create_payment_db
from config import Config, load_config

payment_router = APIRouter()
config: Config = load_config()
bot = Bot(token=config.tg_bot.token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@payment_router.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    pay_id = data.get("object").get("id")
    user_id = data.get("object").get("metadata").get("user_id")
    payment_type = data.get("object").get("metadata").get("payment_type")
    amount = data.get("object").get("amount").get("value")
    currency = data.get("object").get("amount").get("currency")
    status = data.get("event").split(".")[1]

    payment = await get_payment_by_id(pay_id, int(user_id))
    if payment is None and status == "succeeded":
        await create_payment_db(int(user_id),
                                pay_id,
                                float(amount),
                                status,
                                payment_type)

        await process_success_rub_payment(bot,
                                          int(user_id),
                                          amount,
                                          currency)

    return {"status": "ok"}