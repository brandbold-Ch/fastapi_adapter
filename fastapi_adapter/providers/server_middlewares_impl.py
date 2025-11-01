from typing import Any
from fastapi import FastAPI
from nestpy_protocols.webadapters.contracts import BaseServerMiddlewares
from fastapi_adapter.patterns import UniqueInstance


class ServerMiddlewaresImpl(UniqueInstance, BaseServerMiddlewares):

    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self.app = app

    def middleware(self, middleware_type: Any) -> None:
        pass

    def exception_handler(self, exc_class_or_status_code: Any) -> None:
        pass
