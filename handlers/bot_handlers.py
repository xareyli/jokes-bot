from dispatcher import dp, bot
from aiogram.filters.command import Command
from aiogram import types
from aiogram import F
from data import add_group, update_group_publish_frequency, delete_group
from scheduler import schedule_task, update_worker_interval, terminate_worker


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


# Обработчик события удаления бота из группы
@dp.message(F.left_chat_member)
async def handle_bot_left(event: types.ChatMemberUpdated):
    # Получение информации о событии
    chat_id = event.chat.id
    user_id = event.left_chat_member.id

    bot_info = await bot.get_me()

    # Действия, которые нужно выполнить при удалении бота из группы
    if bot_info.id == user_id:
        delete_group(chat_id)
        terminate_worker(chat_id)

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
        update_worker_interval(message.chat.id, hours)

        await message.reply('Интервал успешно обновлён')
    else:
        await message.reply('Произошла ошибка. Интервал не обновлён')
