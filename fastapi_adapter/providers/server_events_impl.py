from fastapi import FastAPI
from nestpy_protocols.webadapters.contracts import BaseServerEvents
from fastapi_adapter.patterns import UniqueInstance


class ServerEventsImpl(UniqueInstance, BaseServerEvents):

    def __init__(self, app: FastAPI) -> None:
        super().__init__()
        self.app = app

    def on_event(self, event_type: str) -> None:
        pass
