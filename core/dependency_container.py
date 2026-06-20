"""
Container de Injeção de Dependências.

Centraliza a criação e o acesso aos objetos compartilhados
da aplicação.

Nesta primeira fase ele possui apenas a infraestrutura básica.

Novos serviços serão registrados nas próximas fases.
"""


class DependencyContainer:
    """
    Container responsável por armazenar
    instâncias compartilhadas.
    """

    def __init__(self):
        self._services = {}

    def register(self, name: str, instance) -> None:
        """
        Registra uma instância.

        Args:
            name: Nome do serviço.
            instance: Objeto registrado.
        """
        self._services[name] = instance

    def resolve(self, name: str):
        """
        Recupera um serviço registrado.

        Args:
            name: Nome do serviço.

        Returns:
            Instância registrada.
        """
        return self._services.get(name)

    def clear(self) -> None:
        """
        Remove todos os serviços registrados.
        """
        self._services.clear()