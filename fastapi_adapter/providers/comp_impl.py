from typing import Any, Dict, List, Sequence
from fastapi import APIRouter
from nestpy_protocols.webprotocols import FrameworkCompProtocol
from fastapi_adapter.utils import ctx_app


class ProviderCompImpl(FrameworkCompProtocol):

    def __init__(self) -> None:
        super().__init__()

    def add_router_group(self, name: str, **kwargs: Any) -> None:
        ctx_app.set(name, APIRouter(**kwargs), "any")

    def add_route_in_router_group(self, name: str, **kwargs: Any) -> None:
        router = ctx_app.get_one(name)
        router["args"].add_api_route(**kwargs)

    def get_router_group(self, router_name: str) -> Any:
        return ctx_app.get_one(router_name)

    def get_router_groups(self) -> List[Any] | Dict[Any, Any] | Sequence[Any]:
        return ctx_app.get_many("any")

    def add_api_route(self, **kwargs: Any) -> None:
        ctx_app.set("add_api_route", kwargs, "comp")

    def add_api_websocket_route(self, **kwargs: Any) -> None:
        ctx_app.set("add_api_websocket_route", kwargs, "comp")

    def websocket(self, **kwargs: Any) -> None:
        ctx_app.set("websocket", kwargs, "comp")

    def include_router_group(self, **kwargs: Any) -> None:
        ctx_app.set("include_router", kwargs, "comp")
