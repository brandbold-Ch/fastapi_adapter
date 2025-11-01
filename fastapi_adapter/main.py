from fastapi import FastAPI
from nestpy_protocols.webadapters import AbstractWebServer
from nestpy_protocols.webadapters.contracts import BaseServerDocs, BaseServerMiddlewares, BaseServerRouter, \
    BaseServerEvents, BaseServerFunctions, BaseServerParams
from fastapi_adapter.patterns import UniqueInstance
from fastapi_adapter.providers import ServerEventsImpl, ServerMiddlewaresImpl, ServerFunctionsImpl, ServerParamsImpl, \
    ServerRouterImpl, ServerDocsImpl
from fastapi_adapter.utils import StorageRouters


class FastAPIAdapter(AbstractWebServer):

    def __init__(self) -> None:
        super().__init__()
        self.app = FastAPI(routers=StorageRouters())

    @property
    def server_params(self) -> BaseServerParams:
        return ServerParamsImpl(self.app)

    @property
    def server_functions(self) -> BaseServerFunctions:
        return ServerFunctionsImpl(self.app)

    @property
    def server_events(self) -> BaseServerEvents:
        return ServerEventsImpl(self.app)

    @property
    def server_router(self) -> BaseServerRouter:
        return ServerRouterImpl(self.app)

    @property
    def server_middlewares(self) -> BaseServerMiddlewares:
        return ServerMiddlewaresImpl(self.app)

    @property
    def server_docs(self) -> BaseServerDocs:
        return ServerDocsImpl(self.app)
