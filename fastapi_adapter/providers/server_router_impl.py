from typing import List, Any, Dict, Sequence, Callable, Optional
from fastapi import FastAPI, APIRouter
from nestpy_protocols.webadapters.contracts import BaseServerRouter


class ServerRouterImpl(BaseServerRouter):

    def __init__(self, app: FastAPI, routers: Dict[str, APIRouter]) -> None:
        self.app = app
        self.routers = routers

    def add_router_group(self, prefix: str, name: str, description: Optional[str] = None,
                         tags: Optional[List[str]] = None, dependencies: Optional[List[Any]] = None,
                         include_in_schema: Optional[bool] = True) -> None:
        router = APIRouter(
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            include_in_schema=include_in_schema
        )
        self.routers[name] = router

    def add_route_in_router_group(self, name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.routers[name].add_api_route(path=path, endpoint=endpoint, **kwargs)

    def get_router_group(self, router_name: str) -> Any:
        return self.routers.get(router_name, None)

    def get_router_groups(self) -> List[Any] | Dict[Any, Any] | Sequence[Any]:
        return self.routers
