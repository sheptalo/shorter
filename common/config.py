from os import environ
from string import ascii_uppercase
from dotenv import load_dotenv

load_dotenv()

DIGITS = ascii_uppercase
BLACK_LIST = environ.get("BLACK_LIST", "").split(",")
URL_TEST = r"^https://.+"
