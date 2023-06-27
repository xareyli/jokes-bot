from dispatcher import dp, bot
from aiogram.filters.command import Command
from aiogram import types
from aiogram import F


# Обработчик события добавления бота в группу
@dp.message(F.new_chat_members)
async def on_chat_member_added(event: types.ChatMemberUpdated):
    bot_info = await bot.get_me()

    # Проверяем, является ли бот добавленным пользователем
    if event.new_chat_member["username"] == bot_info.username:
        await event.reply("Привет! Я добавлен в эту группу.")
