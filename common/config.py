from os import environ
from dotenv import load_dotenv

load_dotenv()

HOST = environ.get('HOST')
DIGITS = 'AdeFybKopx'
BLACK_LIST = environ.get("BLACK_LIST", "").split(",")
URL_TEST = r"^https://.+"
