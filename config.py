from environs import env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class Db:
    host: str
    port: str
    name: str
    user: str
    password: str


@dataclass
class AdminPanel:
    username: str
    password: str
    secret_key: str


@dataclass
class RedisConfig:
    host: str
    port: int
    db: int


@dataclass
class Config:
    tg_bot: TgBot
    db: Db
    admin_panel: AdminPanel
    redis: RedisConfig


def load_config(path: str | None = None) -> Config:
    """Load the config"""
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
        ),
        db=Db(
            host=env.str("DB_HOST", "localhost"),
            port=env.str("DB_PORT", "5432"),
            name=env.str("DB_NAME", "postgres"),
            user=env.str("DB_USER", "postgres"),
            password=env.str("DB_PASS", "postgres"),
        ),
        admin_panel=AdminPanel(
            username=env.str("ADMIN_USERNAME", "admin"),
            password=env.str("ADMIN_PASSWORD", "password"),
            secret_key=env.str("ADMIN_SECRET_KEY", "test_key")
        ),
        redis=RedisConfig(
            host=env.str("REDIS_HOST", "localhost"),
            port=env.int("REDIS_PORT", 6379),
            db=env.int("REDIS_DB", 0),
        )
    )


CURRENT_CAR_NAME_LENGTH = 40
