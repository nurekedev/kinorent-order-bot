import asyncio
import logging
import sys
import config

from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

import core.handlers.basic as handlers

TOKEN = config.settings['TOKEN']
dp = Dispatcher()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(handlers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
