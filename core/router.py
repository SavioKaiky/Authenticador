"""
Router da aplicação.

Responsável pelo gerenciamento das telas utilizando
ScreenManager.

Todas as telas serão registradas aqui.
"""

from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import ScreenManager


class AppRouter:
    """
    Gerencia a navegação da aplicação.
    """

    def __init__(self):
        self.manager = ScreenManager(
            transition=FadeTransition(duration=0.20)
        )

    @property
    def screen_manager(self):
        """
        Retorna o ScreenManager principal.
        """
        return self.manager

    def register(self, screen):
        """
        Registra uma tela.

        Args:
            screen: Instância de Screen.
        """
        self.manager.add_widget(screen)

    def navigate(self, screen_name: str):
        """
        Navega para uma tela.

        Args:
            screen_name: Nome da tela.
        """
        self.manager.current = screen_name

    def current(self):
        """
        Retorna a tela atual.
        """
        return self.manager.current