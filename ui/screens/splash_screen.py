"""
Tela Splash da aplicação.
"""

from kivy.lang import Builder

from ui.screens.base_screen import BaseScreen

Builder.load_file("ui/kv/splash.kv")


class SplashScreen(BaseScreen):
    """
    Primeira tela apresentada ao usuário.
    """

    pass