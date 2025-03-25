from typing import Protocol

from domain import Link


class ILinkRepo(Protocol):
    def create(self, link: Link) -> Link: ...
    def get(self, uid: str) -> Link | None: ...
    def get_last(self) -> Link | None: ...
