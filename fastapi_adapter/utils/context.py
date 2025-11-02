from fastapi_adapter.patterns import UniqueInstance
from typing import Dict, Any, Iterable, Optional, Literal
from fastapi import APIRouter


class  ContextApp(UniqueInstance):

    def __init__(self) -> None:
        self._storage = {}

    def set(self, key: str, value: Any, _as: Literal["conf", "comp", "any"]) -> None:
        self._storage[key] = { "args": value, "as": _as }

    def get_one(self, key: str) -> Dict[str, Any]:
        return self._storage.get(key)

    def get_many(self, _as: Literal["conf", "comp", "any"]) -> Dict[str, Any]:
        result = {}
        for key, val in self._storage.items():
            if val["as"] == _as:
                result[key] = val["args"]
        return result

    def items(self) -> Any:
        return self._storage.items()


class Routers(UniqueInstance):

    def __init__(self) -> None:
        self._routers = {}

    def set(self, key: str, value: APIRouter) -> None:
        self._routers[key] = value

    def get(self, key: str) -> Optional[APIRouter]:
        return self._routers.get(key)

    def items(self) -> Dict[str, APIRouter]:
        return self._routers

    def values(self) -> Iterable[Any]:
        return self._routers.values()

    def keys(self) -> Iterable[Any]:
        return self._routers.keys()


class Conf(UniqueInstance):

    def __init__(self) -> None:
        self._init_params = {}

    def set(self, key: str, value: Any) -> None:
        self._init_params[key] = value

    def items(self) -> Dict[str, Any]:
        return self._init_params


class Comp(UniqueInstance):

    def __init__(self) -> None:
        self._behaviors = {}

    def set(self, key: str, value: Any) -> None:
        self._behaviors[key] = value

    def items(self) -> Dict[str, Any]:
        return self._behaviors


class Docs(UniqueInstance):

    def __init__(self) -> None:
        self._behaviors = {}

    def set(self, key: str, value: Any) -> None:
        self._behaviors[key] = value

    def items(self) -> Dict[str, Any]:
        return self._behaviors


conf = Conf()
routers = Routers()
comp = Comp()
doc = Docs()
ctx_app = ContextApp()
