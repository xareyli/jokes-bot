from dispatcher import dp, bot
from aiogram.filters.command import Command
from aiogram import types
from aiogram import F
from data import add_group, update_group_publish_frequency
from scheduler import schedule_task


async def send_anekdot(group_id):
    await bot.send_message(group_id, "tipa anekdot")


# Обработчик события добавления бота в группу
@dp.message(F.new_chat_members)
async def on_chat_member_added(event: types.ChatMemberUpdated):
    bot_info = await bot.get_me()

    # Проверяем, является ли бот добавленным пользователем
    if event.new_chat_member["username"] == bot_info.username:
        await event.reply("Привет! Я добавлен в эту группу.")
        is_group_added = add_group(event.chat.id)

        if is_group_added:
            schedule_task(event.chat.id, send_anekdot, 3, event.chat.id)


@dp.message(Command('set_hours'))
async def on_set_hours(message: types.Message):
    hours = message.text.split('/set_hours ')[-1]

    try:
        hours = int(hours)

        if not hours or hours > 12 or hours < 1:
            await message.reply('Некорректное значение интервала')
            return False
    except:
        await message.reply('Некорректное значение интервала')
        return False

    is_updated = update_group_publish_frequency(message.chat.id, hours)

    if is_updated:
        await message.reply('Интервал успешно обновлён')
    else:
        await message.reply('Произошла ошибка. Интервал не обновлён')
