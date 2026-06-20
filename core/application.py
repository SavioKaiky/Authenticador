"""
Classe principal da aplicação.

Responsável por:

- Configurar o tema
- Inicializar o container
- Inicializar o Router
- Carregar as telas
"""

from kivymd.app import MDApp

from core.dependency_container import DependencyContainer


class AuthApplication(MDApp):
    """
    Classe principal do aplicativo.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.container = DependencyContainer()

        self.router = None

    def build(self):
        """
        Método chamado automaticamente pelo Kivy.

        Nesta primeira etapa apenas retorna um Widget vazio.

        O Router será implementado no próximo bloco.
        """

        self.title = "Auth App"

        self.theme_cls.theme_style = "Dark"

        self.theme_cls.primary_palette = "Blue"

        from kivy.uix.widget import Widget

        return Widget()