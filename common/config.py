from os import environ
from string import ascii_uppercase
from dotenv import load_dotenv

load_dotenv()

HOST = environ.get('HOST', 'http://127.0.0.1:8000')
DIGITS = 'AdeFybKopx'
BLACK_LIST = environ.get("BLACK_LIST", "").split(",")
URL_TEST = r"^https://.+"
