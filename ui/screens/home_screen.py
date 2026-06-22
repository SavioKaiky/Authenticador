"""
Tela principal (Home) — lista de contas TOTP.
"""

from kivy.lang import Builder

from ui.screens.base_screen import BaseScreen
from ui.widgets.account_card import AccountCard

Builder.load_file("ui/kv/home.kv")


class HomeScreen(BaseScreen):
    """
    Exibe a lista de contas cadastradas com seus códigos TOTP,
    atualizados automaticamente a cada segundo pelo HomeViewModel.
    """

    def on_enter(self, *args) -> None:
        """Inicia o timer e carrega as contas ao entrar na tela."""
        vm = self.container.resolve("home_viewmodel")
        vm.bind(accounts_data=self._on_accounts_changed)
        vm.load()

    def on_leave(self, *args) -> None:
        """Para o timer ao sair da tela, evitando trabalho em background."""
        vm = self.container.resolve("home_viewmodel")
        vm.unbind(accounts_data=self._on_accounts_changed)
        vm.unload()

    def go_to_add_account(self) -> None:
        """Navega para a tela de cadastro de nova conta."""
        self.router.navigate("add_account")

    def _on_accounts_changed(self, instance, accounts_data: list[dict]) -> None:
        """
        Reconstrói os cartões de conta sempre que o ViewModel
        publica uma nova lista (a cada tick do timer).
        """
        container = self.ids.accounts_container
        container.clear_widgets()

        for data in accounts_data:
            card = AccountCard(
                account_id=data["account_id"],
                on_delete=self._remove_account,
            )
            card.account_name = data["name"]
            card.update(data["code"], data["seconds"])
            container.add_widget(card)

    def _remove_account(self, account_id: int) -> None:
        """Remove a conta selecionada, delegando ao ViewModel."""
        vm = self.container.resolve("home_viewmodel")
        vm.remove_account(account_id)