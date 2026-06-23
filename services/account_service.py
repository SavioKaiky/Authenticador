"""
Serviço de gerenciamento de contas.

Orquestra a lógica de negócio entre a UI e o repositório,
sem que nenhum dos dois precise conhecer o outro.
"""

from models.account import Account
from database.repositories.account_repository import AccountRepository
from services.auth_service import AuthService


class AccountService:
    """
    Caso de uso: gerenciar contas 2FA.
    """

    def __init__(
        self,
        repository: AccountRepository,
        auth_service: AuthService,
    ) -> None:
        self._repository = repository
        self._auth = auth_service

    def add_account(self, name: str, secret: str) -> Account:
        """
        Valida, normaliza e cadastra uma nova conta.

        A chave secreta é normalizada antes de persistir:
        espaços removidos e letras convertidas para maiúsculas,
        garantindo que o PyOTP sempre receba um Base32 limpo.

        Args:
            name: Nome da conta (ex: "GitHub").
            secret: Chave Base32 fornecida pelo serviço.

        Returns:
            Conta persistida com id gerado.

        Raises:
            ValueError: Se nome vazio ou secret inválido.
        """
        name = name.strip()
        if not name:
            raise ValueError("O nome da conta não pode ser vazio.")

        secret = secret.strip().upper().replace(" ", "")
        if not secret:
            raise ValueError("A chave secreta não pode ser vazia.")

        if not self._auth.is_valid_secret(secret):
            raise ValueError(
                "Chave secreta inválida. Verifique se copiou corretamente."
            )

        account = Account(name=name, secret=secret)
        return self._repository.save(account)

    def list_accounts(self) -> list[Account]:
        """Retorna todas as contas cadastradas."""
        return self._repository.list_all()

    def remove_account(self, account_id: int) -> bool:
        """
        Remove uma conta pelo id.

        Returns:
            True se removida com sucesso.
        """
        return self._repository.delete(account_id)

    def get_code_for(self, secret: str) -> str:
        """
        Gera o código TOTP atual para uma conta.

        Args:
            secret: Chave da conta.

        Returns:
            Código de 6 dígitos.
        """
        return self._auth.generate_code(secret)