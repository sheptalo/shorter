import asyncio
import os
import logging
import sys

from common.config import HOST
from presentors.fastapi.main import main as fastapi_service
from presentors.cli.main import main as cli_service
from presentors.aiogram.main import main as aiogram_service

async def main(argv):
    if 'cli' in argv:
        return await asyncio.create_task(cli_service(argv))
    fastapi = asyncio.create_task(fastapi_service())
    aiogram = asyncio.create_task(aiogram_service(os.environ.get('BOT_TOKEN')))

    await asyncio.gather(fastapi, aiogram)


if __name__ == "__main__":
    if HOST:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        asyncio.run(main(sys.argv))
    else:
        print("Please set HOST environment variable")

