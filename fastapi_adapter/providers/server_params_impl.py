from typing import Any, Dict, List, Type, Callable, Union

from fastapi import FastAPI
from nestpy_protocols.webadapters.contracts import BaseServerParams


class ServerParamsImpl(BaseServerParams):

    def __init__(self, app: FastAPI) -> None:
        self.app = app

    def set_contact(self, contact: Union[Dict[str, Any], str, None]) -> None:
        self.app.contact = contact

    def set_license(self, license_info: Union[Dict[str, Any], str, None]) -> None:
        self.app.license_info = license_info

    def set_license_url(self, license_url: str) -> None:
        pass

    def set_media_type(self, media_type: str) -> None:
        pass

    def add_middleware(self, middleware_class: Type[Callable], *args, **kwargs) -> None:
        self.app.middleware(middleware_class)

    def set_title(self, title: str) -> None:
        self.app.title = title

    def set_summary(self, summary: str) -> None:
        self.app.summary = summary

    def set_description(self, description: str) -> None:
        self.app.description = description

    def set_version(self, version: str) -> None:
        self.app.version = version

    def set_terms_of_service(self, terms: str) -> None:
        self.app.terms_of_service = terms

    def set_servers(self, servers: List[Dict[str, Any]]) -> None:
        self.app.servers = servers

    def set_root_path_in_servers(self, enabled: bool) -> None:
        self.app.root_path_in_servers = enabled

    def set_separate_input_output_schemas(self, enabled: bool) -> None:
        self.app.separate_input_output_schemas = enabled

    def set_default_response_class(self, response_class: Any) -> None:
        self.app.default_response_class = response_class

    def set_callbacks(self, callbacks: List[Any]) -> None:
        self.app.callbacks = callbacks

    def set_webhooks(self, webhooks: Any) -> None:
        self.app.webhooks = webhooks

    def set_responses(self, responses: Dict[Any, Dict[str, Any]]) -> None:
        self.app.responses = responses

    def set_extra(self, **extra: Any) -> None:
        self.app.extra = extra

    def set_lifespan(self, lifespan: Any) -> None:
        self.app.lifespan = lifespan
