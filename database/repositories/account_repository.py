"""
Repositório de contas — camada de acesso a dados.

Toda interação com o banco passa por aqui,
mantendo os services livres de SQL.
"""

from sqlalchemy.orm import Session

from models.account import Account
from database.session import AccountORM


class AccountRepository:
    """
    CRUD de contas no banco SQLite.
    """

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, account: Account) -> Account:
        """
        Persiste uma nova conta e retorna com o id gerado.
        """
        orm = AccountORM(
            name=account.name,
            secret=account.secret,
            created_at=account.created_at,
        )
        self._session.add(orm)
        self._session.commit()
        self._session.refresh(orm)
        account.id = orm.id
        return account

    def list_all(self) -> list[Account]:
        """
        Retorna todas as contas ordenadas por nome.
        """
        rows = (
            self._session.query(AccountORM)
            .order_by(AccountORM.name)
            .all()
        )
        return [
            Account(id=row.id, name=row.name, secret=row.secret, created_at=row.created_at)
            for row in rows
        ]

    def delete(self, account_id: int) -> bool:
        """
        Remove uma conta pelo id.

        Returns:
            True se removida, False se não encontrada.
        """
        row = self._session.query(AccountORM).filter_by(id=account_id).first()
        if row is None:
            return False
        self._session.delete(row)
        self._session.commit()
        return True
