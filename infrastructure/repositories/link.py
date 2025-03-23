from domain import Link
from domain.interfaces import ILinkRepo


class LinkRepo(ILinkRepo):
    def __init__(self):
        self.links = []

    def create(self, link: Link) -> Link:
        self.links.append(link)
        return link

    def get(self, uid: str) -> Link | None:
        for link in filter(lambda i: i.uid == uid, self.links):
            return link

    def get_last(self) -> Link | None:
        return self.links[-1] if self.links else None
