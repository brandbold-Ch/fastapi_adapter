from typing import Any, Dict, List, Type, Callable, Union
from nestpy_protocols.webadapters.contracts import BaseServerParams


class ServerParamsImpl(BaseServerParams):

    def set_contact(self, contact: Union[Dict[str, Any], str, None]) -> None:
        pass

    def set_license(self, license_info: Union[Dict[str, Any], str, None]) -> None:
        pass

    def set_license_url(self, license_url: str) -> None:
        pass

    def set_media_type(self, media_type: str) -> None:
        pass

    def add_middleware(self, middleware_class: Type[Callable], *args, **kwargs) -> None:
        pass

    def set_title(self, title: str) -> None:
        pass

    def set_summary(self, summary: str) -> None:
        pass

    def set_description(self, description: str) -> None:
        pass

    def set_version(self, version: str) -> None:
        pass

    def set_terms_of_service(self, terms: str) -> None:
        pass

    def set_servers(self, servers: List[Dict[str, Any]]) -> None:
        pass

    def set_root_path_in_servers(self, enabled: bool) -> None:
        pass

    def set_separate_input_output_schemas(self, enabled: bool) -> None:
        pass

    def set_default_response_class(self, response_class: Any) -> None:
        pass

    def set_callbacks(self, callbacks: List[Any]) -> None:
        pass

    def set_webhooks(self, webhooks: Any) -> None:
        pass

    def set_responses(self, responses: Dict[Any, Dict[str, Any]]) -> None:
        pass

    def set_extra(self, **extra: Any) -> None:
        pass

    def set_lifespan(self, lifespan: Any) -> None:
        pass