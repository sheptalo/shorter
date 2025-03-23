from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from common.exceptions import AppException
from domain import Link
from domain.use_cases.link import UCLink

app = FastAPI()


@app.post("/")
@inject
async def create_url(link: Link, use_case: FromDishka[UCLink]):
    try:
        return use_case.create(link)
    except AppException as e:
        return {"error": e.message}


@app.get("/{uid}")
@inject
async def get_url(uid: str, use_case: FromDishka[UCLink]):
    return RedirectResponse(use_case.get(uid), status_code=302)
