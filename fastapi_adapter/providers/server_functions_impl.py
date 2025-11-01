from typing import Union, Any, Callable
from fastapi import FastAPI
from nestpy_protocols.webadapters.contracts import BaseServerFunctions
from fastapi_adapter.patterns import UniqueInstance

class ServerFunctionsImpl(UniqueInstance, BaseServerFunctions):

    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self.app = app

    def add_api_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.app.add_api_route(path, endpoint, **kwargs)

    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.app.add_api_websocket_route(path, endpoint, **kwargs)

    def websocket(self, path: str, **kwargs: Any) -> None:
        self.app.websocket(path, **kwargs)

    def include_router_group(self, router: Any, **kwargs: Any) -> None:
        self.app.include_router(router, **kwargs)

    def trace(self, path: str, **kwargs: Any) -> None:
        self.app.trace(path, **kwargs)

    def set_global_url_prefix(self, prefix: str) -> None:
        self.app.root_path = prefix

    def listen(self, host: str, port: Union[str, int]) -> None:
        for router in self.app.extra["routers"].values():
            self.app.include_router(router=router)
        self.app.extra.clear()

        import uvicorn
        uvicorn.run(self.app, host=host, port=port)
