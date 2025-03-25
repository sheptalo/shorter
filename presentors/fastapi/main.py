import uvicorn

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from common.config import HOST
from infrastructure.di import container
from .handlers import router


async def main():
    try:
        host, port = HOST.split(':')
    except ValueError:
        host = "127.0.0.1"
        port = 8000

    app = FastAPI()
    app.include_router(router)
    setup_dishka(container, app)

    config = uvicorn.Config(app, host=host, port=port)
    server = uvicorn.Server(config)
    await server.serve()
