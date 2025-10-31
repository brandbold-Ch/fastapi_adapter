from typing import Dict, Any, List

from nestpy_protocols.webadapters.contracts import BaseServerDocs


class ServerDocsImp(BaseServerDocs):

    def set_openapi_url(self, url: str) -> None:
        pass

    def set_openapi_tags(self, tags: List[Dict[str, Any]]) -> None:
        pass

    def set_docs_url(self, url: str) -> None:
        pass

    def set_redoc_url(self, url: str) -> None:
        pass

    def set_swagger_ui_oauth2_redirect_url(self, url: str) -> None:
        pass

    def set_swagger_ui_init_oauth(self, config: Any) -> None:
        pass

    def set_swagger_ui_parameters(self, params: Dict[str, Any]) -> None:
        pass

    def set_swagger_ui_url(self, url: str) -> None:
        pass

    def set_swagger_ui_path(self, path: str) -> None:
        pass

    def set_open_api_version(self, version: str) -> None:
        pass

    def set_api_spec_options(self, spect: dict[str, str]) -> None:
        pass
