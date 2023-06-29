from data import get_all_groups, delete_group
from handlers.bot_handlers import send_anekdot
from scheduler import schedule_task
from dispatcher import bot
import asyncio


async def startup_hook():
    groups = get_all_groups()

    bot_info = await bot.get_me()
    bot_id = bot_info.id

    for group in groups:
        try:
            await bot.get_chat_member(chat_id=group[1], user_id=bot_id)

            # исключение не выброшено, бот в группе
            schedule_task(group[1], send_anekdot, group[2], group[1])

            # задержка 3 секунды перед запуском следующего воркера
            await asyncio.sleep(3)
        except:
            # бота удалили
            print(delete_group(group[1]))
