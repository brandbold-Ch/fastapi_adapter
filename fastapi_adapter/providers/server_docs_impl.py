from typing import Dict, Any, List
from nestpy_protocols.webadapters.contracts import BaseServerDocs
from fastapi import FastAPI


class ServerDocsImp(BaseServerDocs):

    def __init__(self, app: FastAPI) -> None:
        self.app = app

    def set_openapi_url(self, url: str) -> None:
        self.app.openapi_url = url

    def set_openapi_tags(self, tags: List[Dict[str, Any]]) -> None:
        self.app.openapi_tags = tags

    def set_docs_url(self, url: str) -> None:
        self.app.docs_url = url

    def set_redoc_url(self, url: str) -> None:
        self.app.redoc_url = url

    def set_swagger_ui_oauth2_redirect_url(self, url: str) -> None:
        self.app.swagger_ui_oauth2_redirect_url = url

    def set_swagger_ui_init_oauth(self, config: Any) -> None:
        self.app.swagger_ui_init_oauth = config

    def set_swagger_ui_parameters(self, params: Dict[str, Any]) -> None:
        self.app.swagger_ui_parameters = params

    def set_swagger_ui_url(self, url: str) -> None:
        ...

    def set_swagger_ui_path(self, path: str) -> None:
        ...

    def set_open_api_version(self, version: str) -> None:
        self.app.openapi_version = version

    def set_api_spec_options(self, spect: dict[str, str]) -> None:
        pass
