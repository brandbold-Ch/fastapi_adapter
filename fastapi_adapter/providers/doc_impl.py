from typing import Any
from nestpy_protocols.webprotocols import FrameworkDocProtocol
from fastapi_adapter.utils import ctx_app


class ProviderDocsImpl(FrameworkDocProtocol):

    def __init__(self) -> None:
        super().__init__()

    def set_openapi_url(self, url: str) -> None:
        ctx_app.set("openapi_url", url, "conf")

    def set_openapi_tags(self, tags: Any) -> None:
        ctx_app.set("openapi_tags", tags, "conf")

    def set_docs_url(self, url: str) -> None:
        ctx_app.set("docs_url", url, "conf")

    def set_redoc_url(self, url: str) -> None:
        ctx_app.set("redoc_url", url, "conf")

    def set_swagger_ui_oauth2_redirect_url(self, url: str) -> None:
        ctx_app.set("swagger_ui_oauth2_redirect_url", url, "conf")

    def set_swagger_ui_init_oauth(self, config: Any) -> None:
        ctx_app.set("swagger_ui_init_oauth", config, "conf")

    def set_swagger_ui_parameters(self, params: Any) -> None:
        ctx_app.set("swagger_ui_parameters", params, "conf")

    def set_swagger_ui_url(self, url: str) -> None:
        ...

    def set_swagger_ui_path(self, path: str) -> None:
        ...

    def set_open_api_version(self, version: str) -> None:
        ctx_app.set("openapi_version", version, "conf")

    def set_api_spec_options(self, spect: Any) -> None:
        pass

    def set_openapi_external_docs(self, external_docs: Any) -> None:
        pass

    def set_include_in_schema(self, include: bool) -> None:
        ctx_app.set("include_in_schema", include, "conf")
