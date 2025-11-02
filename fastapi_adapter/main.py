from nestpy_protocols.webprotocols import FrameworkLifProtocol
from nestpy_protocols.webprotocols.framework.base import FrameworkWebProtocol, FrameworkMwProtocol, \
    FrameworkConfProtocol, FrameworkExcProtocol, FrameworkCompProtocol, FrameworkDocProtocol
from fastapi_adapter.providers import ProviderLifImpl, ProviderMwImpl, ProviderCompImpl, ProviderConfImpl, \
    ProviderDocsImpl, ProviderExcImpl


class FastAPIAdapter(FrameworkWebProtocol):

    @property
    def conf(self) -> FrameworkConfProtocol:
        return ProviderConfImpl()

    @property
    def comp(self) -> FrameworkCompProtocol:
        return ProviderCompImpl()

    @property
    def mw(self) -> FrameworkMwProtocol:
        return ProviderMwImpl()

    @property
    def doc(self) -> FrameworkDocProtocol:
        return ProviderDocsImpl()

    @property
    def exc(self) -> FrameworkExcProtocol:
        return ProviderExcImpl()

    @property
    def lif(self) -> FrameworkLifProtocol:
        return ProviderLifImpl()
