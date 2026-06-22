"""
Gerenciamento do tema da aplicação.
"""

from kivymd.app import MDApp

from core.settings import (
    DEFAULT_THEME,
    PRIMARY_PALETTE,
)


class ThemeManager:
    """
    Configura o tema global da aplicação.
    """

    @staticmethod
    def configure(app: MDApp) -> None:
        """
        Aplica o tema da aplicação.

        Args:
            app: Instância do MDApp.
        """

        app.theme_cls.theme_style = DEFAULT_THEME

        app.theme_cls.primary_palette = PRIMARY_PALETTE