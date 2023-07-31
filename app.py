import logging

from aiogram import executor, Dispatcher

import handlers
from loader import dp
from utils import set_default_commands


async def on_startup(dispatcher: Dispatcher) -> None:
    await set_default_commands(dispatcher)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
