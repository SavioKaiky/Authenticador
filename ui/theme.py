"""
Configuração global do tema da aplicação.
"""

from kivymd.app import MDApp


class ThemeManager:
    """
    Responsável pela configuração visual da aplicação.
    """

    @staticmethod
    def configure(app: MDApp) -> None:
        """
        Configura o tema global.

        Args:
            app: Instância do MDApp.
        """

        app.theme_cls.theme_style = "Dark"

        app.theme_cls.primary_palette = "Blue"

        app.theme_cls.primary_hue = "500"

        app.theme_cls.accent_palette = "Blue"

        app.theme_cls.material_style = "M3"