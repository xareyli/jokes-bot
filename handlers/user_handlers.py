from dispatcher import dp
from aiogram.filters.command import Command
from aiogram import types
from jokes import get_random_joke


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("joke"))
async def cmd_joke(message: types.Message):
    joke = get_random_joke()

    if joke:
        await message.answer(joke)
    else:
        await message.answer(
            "Чёт я начал барахлить, напишите пожалуйста моему разработчику"
        )
