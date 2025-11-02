from typing import Any
from nestpy_protocols.webprotocols import FrameworkConfProtocol
from fastapi_adapter.utils import ctx_app


class ProviderConfImpl(FrameworkConfProtocol):

    def __init__(self) -> None:
        super().__init__()

    def set_debug(self, enabled: bool) -> None:
        ctx_app.set("debug", enabled, "conf")

    def set_contact(self, contact: Any) -> None:
        ctx_app.set("contact", contact, "conf")

    def set_license(self, license_info: Any) -> None:
        ctx_app.set("license_info", license_info, "conf")

    def set_license_url(self, license_url: str) -> None:
        pass

    def set_title(self, title: str) -> None:
        ctx_app.set("title", title, "conf")

    def set_summary(self, summary: str) -> None:
        ctx_app.set("summary", summary, "conf")

    def set_description(self, description: str) -> None:
        ctx_app.set("description", description, "conf")

    def set_version(self, version: str) -> None:
        ctx_app.set("version", version, "conf")

    def set_terms_of_service(self, terms: str) -> None:
        ctx_app.set("terms_of_service", terms, "conf")

    def set_servers(self, servers: Any) -> None:
        ctx_app.set("servers", servers, "conf")

    def set_root_path_in_servers(self, enabled: bool) -> None:
        ctx_app.set("root_path_in_servers", enabled, "conf")

    def set_separate_input_output_schemas(self, enabled: bool) -> None:
        ctx_app.set("separate_input_output_schemas", enabled, "conf")

    def set_default_response_class(self, response_class: Any) -> None:
        ctx_app.set("default_response_class", response_class, "conf")

    def set_callbacks(self, callbacks: Any) -> None:
        ctx_app.set("callbacks", callbacks, "conf")

    def set_webhooks(self, webhooks: Any) -> None:
        ctx_app.set("webhooks", webhooks, "conf")

    def set_responses(self, responses: Any) -> None:
        ctx_app.set("responses", responses, "conf")

    def set_extra(self, **extra: Any) -> None:
        ctx_app.set("extra", extra, "conf")

    def set_lifespan(self, lifespan: Any) -> None:
        ctx_app.set("lifespan", lifespan, "conf")

    def set_global_url_prefix(self, prefix: str) -> None:
        ctx_app.set("root_path", prefix, "conf")

    def set_dependencies(self, dependencies: Any) -> None:
        ctx_app.set("dependencies", dependencies, "conf")

    def set_redirect_slashes(self, enabled: bool) -> None:
        ctx_app.set("redirect_slashes", enabled, "conf")
