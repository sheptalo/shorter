import asyncio

from presentors.fastapi.main import main as fastapi_service
from presentors.cli.main import main as cli_service


async def main(argv):
    if 'cli' in argv:
        cli = asyncio.create_task(cli_service(argv))
        return await cli
    fastapi = asyncio.create_task(fastapi_service())

    await asyncio.gather(fastapi)


if __name__ == "__main__":
    import sys

    asyncio.run(main(sys.argv))
