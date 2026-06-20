"""
Classe principal da aplicação.

Responsável por:

- Configurar o tema global;
- Inicializar os componentes principais;
- Gerenciar o ciclo de vida da aplicação.
"""

from kivy.uix.widget import Widget
from kivymd.app import MDApp

from core.dependency_container import DependencyContainer
from core.lifecycle import ApplicationLifecycle


class AuthApplication(MDApp):
    """
    Classe principal do aplicativo.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.container = DependencyContainer()
        self.lifecycle = ApplicationLifecycle()

    def build(self) -> Widget:
        """
        Constrói a interface principal da aplicação.

        Returns:
            Widget raiz da aplicação.
        """

        self.title = "Auth App"

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return Widget()

    def on_start(self) -> None:
        self.lifecycle.on_start()

    def on_pause(self) -> bool:
        return self.lifecycle.on_pause()

    def on_resume(self) -> None:
        self.lifecycle.on_resume()

    def on_stop(self) -> None:
        self.lifecycle.on_stop()