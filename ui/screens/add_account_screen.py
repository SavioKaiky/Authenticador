"""
Tela de cadastro de nova conta TOTP.
"""

from kivy.lang import Builder

from ui.screens.base_screen import BaseScreen

Builder.load_file("ui/kv/add_account.kv")


class AddAccountScreen(BaseScreen):
    """
    Formulário para adicionar nome + chave secreta.
    """

    def save_account(self) -> None:
        """Valida e persiste a nova conta."""
        name = self.ids.field_name.text.strip()
        secret = self.ids.field_secret.text.strip()

        vm = self.container.resolve("add_account_viewmodel")
        success, error = vm.add_account(name, secret)

        if success:
            self._clear_form()
            self.router.navigate("home")
        else:
            self.ids.lbl_error.text = error

    def go_back(self) -> None:
        """Volta sem salvar."""
        self._clear_form()
        self.router.navigate("home")

    def _clear_form(self) -> None:
        self.ids.field_name.text = ""
        self.ids.field_secret.text = ""
        self.ids.lbl_error.text = ""