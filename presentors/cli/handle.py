from dishka import FromDishka

from domain.use_cases import UCLink
from .decorator import inject

from common.config import HOST
from common.exceptions import AppException


from domain import Link

@inject(is_async=True)
async def create_link(link: str, use_case: FromDishka[UCLink]):
    try:
        return f'{HOST}/{use_case.create(Link(link=link)).uid}'
    except AppException as e:
        return e.message
