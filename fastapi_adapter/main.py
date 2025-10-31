from fastapi import FastAPI
from nestpy_protocols.webadapters import AbstractWebServer
from nestpy_protocols.webadapters.contracts import BaseServerDocs, BaseServerMiddlewares, BaseServerRouter, \
    BaseServerEvents, BaseServerFunctions, BaseServerParams
from fastapi_adapter.providers import ServerEventsImpl, ServerMiddlewaresImpl, ServerFunctionsImpl, ServerParamsImpl, \
    ServerRouterImpl, ServerDocsImp


class FastAPIAdapter(AbstractWebServer):

    def __init__(self):
        self.app = FastAPI()
        self.routers = {}

    def server_params(self) -> BaseServerParams:
        return ServerParamsImpl(self.app)

    def server_functions(self) -> BaseServerFunctions:
        return ServerFunctionsImpl(self.app, self.routers)

    def server_events(self) -> BaseServerEvents:
        return ServerEventsImpl()

    def server_router(self) -> BaseServerRouter:
        return ServerRouterImpl(self.app, self.routers)

    def server_middlewares(self) -> BaseServerMiddlewares:
        return ServerMiddlewaresImpl()

    def server_docs(self) -> BaseServerDocs:
        return ServerDocsImp(self.app)
