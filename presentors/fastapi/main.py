import uvicorn

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from common.config import HOST, PORT
from infrastructure.di import container
from .handlers import router


async def main():
    app = FastAPI()
    app.include_router(router)
    setup_dishka(container, app)

    config = uvicorn.Config(app, host=HOST.split('://')[1], port=PORT)
    server = uvicorn.Server(config)
    await server.serve()
