from fastapi_adapter.patterns import UniqueInstance
from typing import Dict, Any, Iterable, Optional
from fastapi import APIRouter


class StorageRouters(UniqueInstance):

    def __init__(self) -> None:
        self._storage = {}

    def set(self, key: str, value: APIRouter) -> None:
        self._storage[key] = value

    def get(self, key: str) -> Optional[APIRouter]:
        return self._storage.get(key)

    def all(self) -> Dict[str, APIRouter]:
        return self._storage

    def values(self) -> Iterable[Any]:
        return self._storage.values()

    def keys(self) -> Iterable[Any]:
        return self._storage.keys()
