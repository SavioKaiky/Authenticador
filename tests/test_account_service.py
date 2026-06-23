"""
Testes de integração do AccountService.

Usa banco SQLite em memória (:memory:) para isolar os testes
do banco real em ~/.auth_app/auth.db.
"""

import pytest

from database.database import Database
from database.repositories.account_repository import AccountRepository
from services.account_service import AccountService
from services.auth_service import AuthService


VALID_SECRET = "JBSWY3DPEHPK3PXP"


@pytest.fixture
def service() -> AccountService:
    """
    Cria um AccountService completo usando banco em memória.
    Cada teste recebe um banco limpo e isolado.
    """
    db = Database(db_path=":memory:")
    db.create_tables()
    session = db.get_session()
    repository = AccountRepository(session)
    auth = AuthService()
    return AccountService(repository=repository, auth_service=auth)


class TestAddAccount:

    def test_adiciona_conta_valida(self, service):
        account = service.add_account("GitHub", VALID_SECRET)
        assert account.id is not None
        assert account.name == "GitHub"

    def test_normaliza_secret_para_maiusculo(self, service):
        account = service.add_account("GitHub", VALID_SECRET.lower())
        assert account.secret == VALID_SECRET.upper()

    def test_remove_espacos_do_secret(self, service):
        account = service.add_account("GitHub", "JBSWY3DP EHPK3PXP")
        assert " " not in account.secret

    def test_nome_vazio_lanca_value_error(self, service):
        with pytest.raises(ValueError, match="nome"):
            service.add_account("", VALID_SECRET)

    def test_nome_so_espacos_lanca_value_error(self, service):
        with pytest.raises(ValueError, match="nome"):
            service.add_account("   ", VALID_SECRET)

    def test_secret_invalido_lanca_value_error(self, service):
        with pytest.raises(ValueError, match="[Cc]have"):
            service.add_account("GitHub", "CHAVE_INVALIDA")

    def test_secret_vazio_lanca_value_error(self, service):
        with pytest.raises(ValueError):
            service.add_account("GitHub", "")


class TestListAccounts:

    def test_lista_vazia_sem_contas(self, service):
        assert service.list_accounts() == []

    def test_lista_conta_apos_adicionar(self, service):
        service.add_account("GitHub", VALID_SECRET)
        accounts = service.list_accounts()
        assert len(accounts) == 1
        assert accounts[0].name == "GitHub"

    def test_lista_ordenada_por_nome(self, service):
        service.add_account("Zello", VALID_SECRET)
        service.add_account("Amazon", VALID_SECRET)
        service.add_account("Microsoft", VALID_SECRET)
        names = [a.name for a in service.list_accounts()]
        assert names == sorted(names)


class TestRemoveAccount:

    def test_remove_conta_existente(self, service):
        account = service.add_account("GitHub", VALID_SECRET)
        result = service.remove_account(account.id)
        assert result is True
        assert service.list_accounts() == []

    def test_remover_id_inexistente_retorna_false(self, service):
        result = service.remove_account(999)
        assert result is False


class TestGetCodeFor:

    def test_retorna_codigo_de_6_digitos(self, service):
        code = service.get_code_for(VALID_SECRET)
        assert len(code) == 6
        assert code.isdigit()