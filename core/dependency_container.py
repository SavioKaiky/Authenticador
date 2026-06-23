"""
Container de Injeção de Dependências.

Registra e resolve todas as dependências da aplicação
em um único lugar, garantindo acoplamento mínimo.
"""

from typing import Any, Callable


class DependencyContainer:
    """Container de singletons e factories."""

    def __init__(self) -> None:
        self._singletons: dict[str, Any] = {}
        self._factories: dict[str, Callable[[], Any]] = {}

    def register_singleton(self, key: str, instance: Any) -> None:
        self._singletons[key] = instance

    def register_factory(self, key: str, factory: Callable[[], Any]) -> None:
        self._factories[key] = factory

    def resolve(self, key: str) -> Any:
        if key in self._singletons:
            return self._singletons[key]
        if key in self._factories:
            return self._factories[key]()
        raise KeyError(f"Dependência '{key}' não encontrada.")

    def clear(self) -> None:
        self._singletons.clear()
        self._factories.clear()
