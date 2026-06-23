"""
Widget visual de cartão de conta TOTP.
"""

from typing import Callable

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty


class AccountCard(MDBoxLayout):
    """
    Exibe o nome, o código TOTP e o contador regressivo de uma conta.
    Emite on_delete quando o botão de exclusão é pressionado.
    """

    account_name = StringProperty("")
    totp_code = StringProperty("------")
    seconds = NumericProperty(30)

    def __init__(
        self,
        account_id: int,
        on_delete: Callable[[int], None],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._account_id = account_id
        self._on_delete_callback = on_delete

    def on_delete(self) -> None:
        """Chamado pelo botão de lixeira."""
        self._on_delete_callback(self._account_id)

    def update(self, code: str, seconds: int) -> None:
        """Atualiza código e contador sem recriar o widget."""
        self.totp_code = code
        self.seconds = seconds
