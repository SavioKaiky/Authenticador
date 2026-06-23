"""
Inicialização e migrações do banco de dados.

Ponto único de entrada para setup do banco.
"""

from database.database import Database
from database.session import AccountORM  # noqa: F401 — garante que o ORM seja registrado


def initialize_database(db: Database) -> None:
    """
    Cria as tabelas e executa migrações necessárias.

    Args:
        db: Instância do Database já configurada.
    """
    db.create_tables()
