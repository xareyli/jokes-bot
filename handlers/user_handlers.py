from dispatcher import dp
from aiogram.filters.command import Command
from aiogram import types


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
