from typing import List, Any, Dict, Sequence, Callable, Optional
from fastapi import FastAPI, APIRouter
from nestpy_protocols.webadapters.contracts import BaseServerRouter
from fastapi_adapter.patterns import UniqueInstance


class ServerRouterImpl(UniqueInstance, BaseServerRouter):

    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self.app = app

    def add_router_group(self, prefix: str, name: str, description: Optional[str] = None,
                         tags: Optional[List[str]] = None, dependencies: Optional[List[Any]] = None,
                         include_in_schema: Optional[bool] = True) -> None:
        router = APIRouter(
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            include_in_schema=include_in_schema
        )
        self.app.extra["routers"].set(name, router)

    def add_route_in_router_group(self, name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        item = self.app.extra["routers"].get(name)
        if item:
            item.add_api_route(path, endpoint, **kwargs)

    def get_router_group(self, router_name: str) -> Any:
        return self.app.extra["routers"].get(router_name)

    def get_router_groups(self) -> List[Any] | Dict[Any, Any] | Sequence[Any]:
        return self.app.extra["routers"].all()
