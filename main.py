from infrastructure.di import container
from dishka.integrations.fastapi import setup_dishka
from presentors.fastapi.main import app

setup_dishka(container, app)
