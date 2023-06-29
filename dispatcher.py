import logging
from aiogram import Bot, Dispatcher
from config import conf


if not conf.bot.token:
    exit("No token provided")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=conf.logging_level)

bot = Bot(token=conf.bot.token)
dp = Dispatcher()
