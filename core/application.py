"""
Classe principal da aplicação.

Responsável por:

- Configurar o tema global;
- Inicializar os componentes principais;
- Gerenciar o ciclo de vida da aplicação.

Nesta primeira etapa a aplicação retorna apenas um Widget vazio.
Nas próximas etapas o Router substituirá esse Widget.
"""

from kivy.uix.widget import Widget
from kivymd.app import MDApp


class AuthApplication(MDApp):
    """
    Classe principal do aplicativo.
    """

    def __init__(self, **kwargs) -> None:
        """
        Inicializa a aplicação.

        Args:
            **kwargs: Argumentos repassados ao MDApp.
        """
        super().__init__(**kwargs)

    def build(self) -> Widget:
        """
        Constrói a interface principal da aplicação.

        Returns:
            Widget: Widget raiz da aplicação.
        """

        self.title = "Auth App"

        # Tema temporário.
        # Será movido para ThemeManager na próxima etapa.
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return Widget()

    def on_start(self) -> None:
        """
        Executado quando a aplicação inicia.
        """
        print("[INFO] Auth App iniciado.")

    def on_stop(self) -> None:
        """
        Executado quando a aplicação é encerrada.
        """
        print("[INFO] Auth App encerrado.")