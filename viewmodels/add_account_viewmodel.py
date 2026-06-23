"""
ViewModel da tela de adição de contas.
"""

from services.account_service import AccountService


class AddAccountViewModel:
    """
    Lógica de validação e persistência ao adicionar uma conta.
    """

    def __init__(self, account_service: AccountService) -> None:
        self._account_service = account_service

    def add_account(self, name: str, secret: str) -> tuple[bool, str]:
        """
        Tenta adicionar uma conta.

        Returns:
            (True, "") em caso de sucesso.
            (False, mensagem_de_erro) em caso de falha.
        """
        try:
            self._account_service.add_account(name, secret)
            return True, ""
        except ValueError as e:
            return False, str(e)
