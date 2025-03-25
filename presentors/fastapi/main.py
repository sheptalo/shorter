import uvicorn

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from common.config import PORT, DEBUG
from infrastructure.di import container
from .handlers import router


async def main():
    app = FastAPI()
    app.include_router(router)
    setup_dishka(container, app)
    host = '0.0.0.0' if not DEBUG else '127.0.0.1'
    config = uvicorn.Config(app, host=host, port=PORT)
    server = uvicorn.Server(config)
    await server.serve()
