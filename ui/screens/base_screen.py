"""
Classe base de todas as telas da aplicação.
"""

from kivy.uix.screenmanager import Screen
from kivy.app import App


class BaseScreen(Screen):
    """
    Tela base utilizada por todas as outras telas.
    """

    @property
    def application(self):
        """
        Retorna a instância principal da aplicação.
        """

        return App.get_running_app()

    @property
    def router(self):
        """
        Retorna o Router principal.
        """

        return self.application.router

    @property
    def container(self):
        """
        Retorna o Dependency Container.
        """

        return self.application.container