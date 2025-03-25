from domain import Link
from domain.interfaces import ILinkRepo
import sqlite3


class MemoryLinkRepo(ILinkRepo):
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


class SQLiteLinkRepo(ILinkRepo):

    def __init__(self):
        self.conn = sqlite3.connect('links.db')
        self.cursor = self.conn.cursor()

        cursor = self.cursor
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS links (
        uid STRING PRIMARY KEY,
        link STRING
        )""")
        self.conn.commit()

    def create(self, link: Link) -> Link:
        print(link)
        self.cursor.execute(
            """INSERT INTO links (uid, link) VALUES (?, ?)""",
            (link.uid, link.link)
            )
        self.conn.commit()
        return link

    def get(self, uid: str) -> Link | None:
        self.cursor.execute(
            "SELECT * FROM links WHERE uid = ?", (uid,)
        )
        result = self.cursor.fetchone()
        print(result)

        if not result:
            return None
        return Link(link=result[1], uid=result[0])

    def get_last(self) -> Link | None:
        self.cursor.execute(
            "SELECT * FROM links ORDER BY uid DESC LIMIT 1"
        )
        result = self.cursor.fetchone()
        if not result:
            return None
        return Link(link=result[1], uid=result[0])
