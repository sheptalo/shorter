from dishka import FromDishka
from dishka.integrations.base import wrap_injection

from common.config import HOST
from common.exceptions import AppException
from domain.use_cases import UCLink
from infrastructure.di import container
from domain import Link



def dec(func):
    return wrap_injection(
        func=func,
        container_getter=lambda _, __: container,
        is_async=True,
    )


@dec
async def main(argv, use_case: FromDishka[UCLink]):
    try:
        link = argv[argv.index('cli') + 1]
    except ValueError:
        link = None
    if not link:
        print("No link provided")
        exit(1)
    try:
        print(f'{HOST}/{use_case.create(Link(link=link)).uid}')
    except AppException as e:
        print(e.message)