from dishka.integrations.aiogram import setup_dishka

from infrastructure.di import container
from presentors.aiogram.handlers import router
import logging
from aiogram import Bot, Dispatcher


async def main(token=None):
    if not token:
        logging.warning('Не предоставлен токен бота, SKIP...')
        return
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    setup_dishka(container, dp)
    await dp.start_polling(bot, skip_updates=True)
