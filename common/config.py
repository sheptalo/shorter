from os import environ
from dotenv import load_dotenv

load_dotenv()

HOST = environ.get("HOST")
PORT = environ.get("PORT", 80)
DIGITS = "AdeFybKopx"
BLACK_LIST = environ.get("BLACK_LIST", "").split(",")
URL_TEST = r"^https://.+"


def full_path():
    return HOST + (f":{PORT}" if PORT != 80 else "")
