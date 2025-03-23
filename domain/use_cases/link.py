from re import findall

from common import config
from domain import Link
from domain.interfaces import ILinkRepo
from common.exceptions import BlackListError, InvalidURLError


class UCLink:
    def __init__(self, repo: ILinkRepo):
        self.repo = repo

    def create(self, link: Link) -> Link:
        for url in config.BLACK_LIST:
            if link.link.startswith(url):
                raise BlackListError
        result = findall(config.URL_TEST, link.link)
        if not result:
            raise InvalidURLError
        last = self.repo.get_last()
        link.generate_uid(last.uid) if last else link.generate_uid("DFER")
        return self.repo.create(link)

    def get(self, uid: str) -> str:
        result = self.repo.get(uid)
        return result.link if result else "/"
