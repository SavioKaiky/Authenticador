"""
Classe principal da aplicação.
"""

from kivymd.app import MDApp

from core.dependency_container import DependencyContainer
from core.lifecycle import ApplicationLifecycle
from core.router import AppRouter
from core.settings import APP_NAME

from ui.theme import ThemeManager


class AuthApplication(MDApp):
    """
    Classe principal da aplicação.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.container = DependencyContainer()

        self.router = AppRouter()

        self.lifecycle = ApplicationLifecycle()

    def build(self):

        self.title = APP_NAME

        ThemeManager.configure(self)

        return self.router.manager

    def on_start(self):
        self.lifecycle.on_start()

    def on_pause(self):
        return self.lifecycle.on_pause()

    def on_resume(self):
        self.lifecycle.on_resume()

    def on_stop(self):
        self.lifecycle.on_stop()