""" This file represents configurations from files and environment"""
import logging
from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv


load_dotenv()


@dataclass
class SchedulerConfig:
    """Asynchronous scheduler configuration"""

    max_instances: int = int(getenv("MAX_GROUPS", 5))
    workers_startup_delay: int = int(getenv("WORKERS_STARTUP_DELAY", 3))


@dataclass
class BotConfig:
    """Bot configuration"""

    token: str = getenv("BOT_TOKEN")


@dataclass
class Configuration:
    """All in one configuration's class"""

    debug = bool(getenv("DEBUG"))
    logging_level = int(getenv("LOGGING_LEVEL", logging.INFO))

    scheduler = SchedulerConfig()
    bot = BotConfig()


conf = Configuration()
