from typing import Union, Any, Callable
from nestpy_protocols.webadapters.contracts import BaseServerFunctions


class ServerFunctionsImpl(BaseServerFunctions):

    def add_api_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        pass

    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        pass

    def websocket(self, path: str, **kwargs: Any) -> None:
        pass

    def include_router_group(self, router: Any, **kwargs: Any) -> None:
        pass

    def trace(self, path: str, **kwargs: Any) -> None:
        pass

    def set_global_url_prefix(self, prefix: str) -> None:
        pass

    def listen(self, host: str, port: Union[str, int]) -> None:
        pass