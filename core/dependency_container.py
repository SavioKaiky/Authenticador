"""
Container de Injeção de Dependências.

Responsável por registrar e resolver as dependências da aplicação.

Esta implementação já suporta:

- Singleton
- Factory

Preparada para futuras expansões.
"""

from typing import Any, Callable


class DependencyContainer:
    """
    Container responsável por gerenciar as dependências
    da aplicação.
    """

    def __init__(self) -> None:
        self._singletons: dict[str, Any] = {}
        self._factories: dict[str, Callable[[], Any]] = {}

    def register_singleton(self, key: str, instance: Any) -> None:
        """
        Registra uma instância singleton.

        Args:
            key: Nome da dependência.
            instance: Instância a ser registrada.
        """
        self._singletons[key] = instance

    def register_factory(
        self,
        key: str,
        factory: Callable[[], Any],
    ) -> None:
        """
        Registra uma fábrica.

        Args:
            key: Nome da dependência.
            factory: Função responsável por criar a instância.
        """
        self._factories[key] = factory

    def resolve(self, key: str) -> Any:
        """
        Obtém uma dependência registrada.

        Args:
            key: Nome da dependência.

        Returns:
            Instância solicitada.

        Raises:
            KeyError: Caso a dependência não exista.
        """

        if key in self._singletons:
            return self._singletons[key]

        if key in self._factories:
            return self._factories[key]()

        raise KeyError(f"Dependência '{key}' não encontrada.")

    def clear(self) -> None:
        """
        Remove todas as dependências registradas.
        """

        self._singletons.clear()
        self._factories.clear()