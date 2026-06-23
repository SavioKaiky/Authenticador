"""
ViewModel da tela principal (Home).

Gerencia o estado das contas e dos códigos TOTP,
expondo apenas o necessário para a View.
"""

from kivy.event import EventDispatcher
from kivy.properties import ListProperty, NumericProperty

from models.account import Account
from services.account_service import AccountService
from services.timer_service import TimerService


class HomeViewModel(EventDispatcher):
    """
    Estado reativo da tela Home.

    accounts_data: lista de dicionários prontos para a RecycleView.
    seconds_remaining: segundos até o próximo refresh.
    """

    accounts_data = ListProperty([])
    seconds_remaining = NumericProperty(30)

    def __init__(
        self,
        account_service: AccountService,
        timer_service: TimerService,
    ) -> None:
        super().__init__()
        self._account_service = account_service
        self._timer = timer_service

    def load(self) -> None:
        """Carrega contas e inicia o timer de atualização."""
        self._refresh()
        self._timer.start(self._refresh)

    def unload(self) -> None:
        """Para o timer ao sair da tela."""
        self._timer.stop()

    def remove_account(self, account_id: int) -> None:
        """Remove uma conta e atualiza a lista."""
        self._account_service.remove_account(account_id)
        self._refresh()

    def _refresh(self) -> None:
        """Atualiza códigos e contador — chamado a cada segundo."""
        accounts = self._account_service.list_accounts()
        self.seconds_remaining = self._timer.seconds_remaining()
        self.accounts_data = [
            {
                "account_id": acc.id,
                "name": acc.name,
                "code": self._account_service.get_code_for(acc.secret),
                "seconds": self.seconds_remaining,
            }
            for acc in accounts
        ]
