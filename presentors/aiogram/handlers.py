from aiogram import Router, F, types
from dishka import FromDishka
from dishka.integrations.aiogram import inject

from common.config import HOST
from domain import Link
from domain.use_cases import UCLink
from .messages import welcome

router = Router()

@router.message(F.text.startswith('/start'))
async def start(message: types.Message):
    return await message.answer(welcome)

@router.message(F.text.startswith('https://'))
@inject
async def create_url(message: types.Message, use_case: FromDishka[UCLink]):
    try:
        await message.answer(f'Ссылка: {HOST}/{use_case.create(Link(link=message.text)).uid}')
    except Exception as e:
        await message.answer('Произошла ошибка попробуйте позже')