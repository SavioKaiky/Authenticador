"""
Classe principal da aplicação.
"""

from kivymd.app import MDApp

from core.dependency_container import DependencyContainer
from core.lifecycle import ApplicationLifecycle
from core.router import AppRouter

from ui.theme import ThemeManager
from ui.screens.splash_screen import SplashScreen


class AuthApplication(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.container = DependencyContainer()

        self.router = AppRouter()

        self.lifecycle = ApplicationLifecycle()

    def build(self):

        self.title = "Auth App"

        ThemeManager.configure(self)

        self.router.register(
            SplashScreen()
        )

        return self.router.screen_manager

    def on_start(self):
        self.lifecycle.on_start()

    def on_pause(self):
        return self.lifecycle.on_pause()

    def on_resume(self):
        self.lifecycle.on_resume()

    def on_stop(self):
        self.lifecycle.on_stop()