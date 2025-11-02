from typing import Any
from nestpy_protocols.webprotocols import FrameworkMwProtocol


class ProviderMwImpl(FrameworkMwProtocol):

    def __init__(self) -> None:
        super().__init__()

    def global_middleware(self, middleware: Any) -> None:
        pass

    def add_middlewares(self, middlewares: Any) -> None:
        pass

    def trace(self, **kwargs: Any) -> None:
        pass
