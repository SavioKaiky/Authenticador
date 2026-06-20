"""
Gerenciador de navegação da aplicação.
"""

from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager


class AppRouter:
    """
    Responsável pela navegação entre telas.
    """

    def __init__(self) -> None:

        self._manager = ScreenManager(
            transition=FadeTransition(duration=0.20)
        )

    @property
    def manager(self) -> ScreenManager:
        """
        Retorna o ScreenManager.
        """

        return self._manager

    def register(self, screen: Screen) -> None:
        """
        Registra uma tela.

        Args:
            screen: Instância da tela.
        """

        self._manager.add_widget(screen)

    def navigate(self, screen_name: str) -> None:
        """
        Navega para uma tela.

        Args:
            screen_name: Nome da tela.
        """

        self._manager.current = screen_name

    @property
    def current(self) -> str:
        """
        Nome da tela atual.
        """

        return self._manager.current