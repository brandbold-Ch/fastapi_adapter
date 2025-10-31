from nestpy_protocols.webadapters.contracts import BaseServerEvents


class ServerEventsImpl(BaseServerEvents):

    def on_event(self, event_type: str) -> None:
        pass