import asyncio
from dispatcher import dp, bot
from startup import startup_hook

import handlers


async def main():
    await startup_hook()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
