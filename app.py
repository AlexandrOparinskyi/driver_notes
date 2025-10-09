import asyncio
import json
import logging
from datetime import datetime, date
from typing import Any

from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from I18N import create_translator_hub
from bot import bot

from config import Config, load_config

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


def custom_json_dumps(obj: Any) -> str:
    """Custom serialization for datetime"""

    def default_encoder(o):
        if isinstance(o, (datetime, date)):
            return {'__type__': 'datetime', 'value': o.strftime("%d.%m.%Y")}
        return str(o)

    return json.dumps(obj, default=default_encoder, ensure_ascii=False)


def custom_json_loads(data: str) -> Any:
    """Custom deserialization with datetime recovery"""

    def object_hook(obj):
        if '__type__' in obj and obj['__type__'] == 'datetime':
            return datetime.strptime(obj.get("value"), "%d.%m.%Y")
        return obj

    result = json.loads(data, object_hook=object_hook)
    return result if isinstance(result, dict) else {}


async def main() -> None:
    config: Config = load_config()
    translator_hub = create_translator_hub()

    redis_client = Redis(
        host=config.redis.host,
        port=config.redis.port,
        db=config.redis.db,
        decode_responses=False
    )
    storage = RedisStorage(
        redis_client,
        key_builder=DefaultKeyBuilder(with_destiny=True, prefix='bot_fsm'),
        json_loads=custom_json_loads,
        json_dumps=custom_json_dumps
    )

    await asyncio.gather(bot(
        config.tg_bot.token,
        translator_hub,
        # storage
    ))


if __name__ == "__main__":
    asyncio.run(main())
