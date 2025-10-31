from typing import Any

from nestpy_protocols.webadapters.contracts import BaseServerMiddlewares


class ServerMiddlewaresImpl(BaseServerMiddlewares):

    def middleware(self, middleware_type: Any) -> None:
        pass

    def exception_handler(self, exc_class_or_status_code: Any) -> None:
        pass
