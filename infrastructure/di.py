from dishka import Provider, Scope, make_async_container

from domain.interfaces import ILinkRepo
from domain.use_cases import UCLink
from infrastructure.repositories import MemoryLinkRepo
from infrastructure.repositories.link import SQLiteLinkRepo

provider = Provider()
# provider.provide(MemoryLinkRepo, provides=ILinkRepo, scope=Scope.APP)
provider.provide(SQLiteLinkRepo, provides=ILinkRepo, scope=Scope.APP)
provider.provide(UCLink, scope=Scope.APP)

container = make_async_container(provider)
