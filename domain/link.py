from pydantic import BaseModel

from common.config import DIGITS


class Link(BaseModel):
    link: str
    uid: str = None

    def generate_uid(self, last_uid: str) -> None:
        parsed_int = int("".join([str(DIGITS.index(i)) for i in last_uid]))
        self.uid = "".join(DIGITS[int(i)] for i in str(parsed_int + 1))
