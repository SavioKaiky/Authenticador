"""
Gerenciamento do ciclo de vida da aplicação.
"""

import logging


logger = logging.getLogger(__name__)


class ApplicationLifecycle:
    """
    Centraliza os eventos do ciclo de vida da aplicação.
    """

    def on_start(self) -> None:
        """
        Executado quando a aplicação é iniciada.
        """
        logger.info("Aplicação iniciada.")

    def on_pause(self) -> bool:
        """
        Executado quando a aplicação vai para segundo plano.

        Returns:
            True para permitir a pausa.
        """
        logger.info("Aplicação pausada.")
        return True

    def on_resume(self) -> None:
        """
        Executado quando a aplicação retorna ao primeiro plano.
        """
        logger.info("Aplicação retomada.")

    def on_stop(self) -> None:
        """
        Executado antes do encerramento da aplicação.
        """
        logger.info("Aplicação encerrada.")