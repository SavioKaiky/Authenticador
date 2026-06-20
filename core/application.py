"""
Classe principal da aplicação.

Responsável por:

- Configurar o tema
- Inicializar o container
- Inicializar o Router
- Gerenciar o ciclo de vida
"""

from kivymd.app import MDApp

from core.dependency_container import DependencyContainer
from core.lifecycle import ApplicationLifecycle
from core.router import AppRouter


class AuthApplication(MDApp):
    """
    Classe principal do aplicativo.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.container = DependencyContainer()

        self.router = AppRouter()

        self.lifecycle = ApplicationLifecycle()

    def build(self):
        """
        Inicializa a aplicação.
        """

        self.title = "Auth App"

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return self.router.screen_manager

    def on_start(self):
        self.lifecycle.on_start()

    def on_pause(self):
        return self.lifecycle.on_pause()

    def on_resume(self):
        self.lifecycle.on_resume()

    def on_stop(self):
        self.lifecycle.on_stop()