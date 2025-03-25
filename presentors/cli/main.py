
from .handle import create_link


async def main(argv):
    try:
        result = await create_link(link=argv[2])
    except Exception as e:
        print(e)
        result = "Предоставьте URL адрес сайта"
    print(result)