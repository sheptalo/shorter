from os import environ
from dotenv import load_dotenv

load_dotenv()

HOST = environ.get("HOST")
PORT = int(environ.get("PORT", 80))
DEBUG = environ.get("DEBUG") != "False"
DIGITS = "AdeFybKopx"
BLACK_LIST = environ.get("BLACK_LIST", "").split(",")
URL_TEST = r"^https://.+"


def full_path():
    host = HOST if not DEBUG else 'http://127.0.0.1'
    return host + (f":{PORT}" if PORT != 80 else "")
