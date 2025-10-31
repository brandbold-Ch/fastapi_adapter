from typing import List, Any, Dict, Sequence, Callable, Optional
from nestpy_protocols.webadapters.contracts import BaseServerRouter


class ServerRouterImpl(BaseServerRouter):

    def add_router_group(self, prefix: str, name: str, description: Optional[str] = None,
                         tags: Optional[List[str]] = None, dependencies: Optional[List[Any]] = None,
                         include_in_schema: Optional[bool] = True) -> None:
        pass

    def add_route_in_router_group(self, name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        pass

    def get_router_group(self, router_name: str) -> Any:
        pass

    def get_router_groups(self) -> List[Any] | Dict[Any, Any] | Sequence[Any]:
        pass