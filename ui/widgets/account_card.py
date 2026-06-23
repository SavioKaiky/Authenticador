"""
Widget visual de cartão de conta TOTP.
"""

from typing import Callable

from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogButtonContainer,
    MDDialogHeadlineText,
    MDDialogSupportingText,
)
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


class AccountCard(MDBoxLayout):
    """
    Exibe o nome, o código TOTP e o contador regressivo de uma conta.

    - Toque no código: copia para o clipboard e exibe snackbar de confirmação.
    - Toque na lixeira: exibe diálogo de confirmação antes de remover.
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
        self._dialog = None

    def copy_code(self) -> None:
        """Copia o código TOTP atual para o clipboard e exibe feedback."""
        from kivy.core.clipboard import Clipboard
        Clipboard.copy(self.totp_code)
        MDSnackbar(
            MDSnackbarText(
                text=f"Código copiado: {self.totp_code}",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
        ).open()

    def on_delete(self) -> None:
        """Exibe o diálogo de confirmação ao tocar na lixeira."""
        self._dialog = MDDialog(
            MDDialogHeadlineText(
                text="Remover conta?",
            ),
            MDDialogSupportingText(
                text=f'A conta "{self.account_name}" será removida permanentemente.',
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancelar"),
                    style="text",
                    on_release=self._dismiss_dialog,
                ),
                MDButton(
                    MDButtonText(text="Remover"),
                    style="text",
                    on_release=self._confirm_delete,
                ),
                spacing="8dp",
            ),
        )
        self._dialog.open()

    def update(self, code: str, seconds: int) -> None:
        """Atualiza código e contador sem recriar o widget."""
        self.totp_code = code
        self.seconds = seconds

    def _confirm_delete(self, *args) -> None:
        """Fecha o diálogo e dispara o callback de exclusão."""
        self._dismiss_dialog()
        self._on_delete_callback(self._account_id)

    def _dismiss_dialog(self, *args) -> None:
        """Fecha o diálogo sem realizar nenhuma ação."""
        if self._dialog:
            self._dialog.dismiss()
            self._dialog = None