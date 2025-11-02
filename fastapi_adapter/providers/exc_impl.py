from typing import Any
from nestpy_protocols.webprotocols import FrameworkExcProtocol


class ProviderExcImpl(FrameworkExcProtocol):

    def __init__(self) -> None:
        super().__init__()

    def global_exception_handler(self, exc_class_or_status_code: Any) -> None:
        pass

    def set_exception_handlers(self, handlers: Any) -> None:
        pass
