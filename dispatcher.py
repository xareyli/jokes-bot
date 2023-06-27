import logging
from aiogram import Bot, Dispatcher

import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("BOT_TOKEN"):
    exit("No token provided")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
