from os import environ
from dotenv import load_dotenv

load_dotenv()

HOST = environ.get("HOST")
DEBUG = environ.get("DEBUG") != "False"
DIGITS = "AdeFybKopx"
BLACK_LIST = environ.get("BLACK_LIST", "").split(",")
URL_TEST = r"^https://.+"


def full_path():
    return HOST if not DEBUG else 'http://127.0.0.1'