from typing import Union, Any
from nestpy_protocols.webprotocols import FrameworkLifProtocol
from fastapi_adapter.patterns import UniqueInstance
from fastapi_adapter.utils import ctx_app
from fastapi import FastAPI


class ProviderLifImpl(UniqueInstance, FrameworkLifProtocol):

    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event_type: str) -> None:
        pass

    def set_on_startup(self, handlers: Any) -> None:
        pass

    def set_on_shutdown(self, handlers: Any) -> None:
        pass

    def stop_server(self) -> None:
        pass

    def start_server(self, host: str, port: Union[str, int]) -> None:
        app = FastAPI(**ctx_app.get_many("conf"))

        for k, v in ctx_app.items():
            print(k, v)
            if v["as"] == "comp":
                getattr(app, k)(**v["args"])
            elif v["as"] == "any":
                app.include_router(v["args"])

        import uvicorn
        uvicorn.run(app, host=host, port=port)
