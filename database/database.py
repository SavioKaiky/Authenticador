"""
Configuração e inicialização do banco de dados SQLite.

O banco é criado no diretório de dados do usuário
para garantir persistência entre sessões.
"""

import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from database.base import Base


def _get_db_path() -> str:
    """
    Retorna o caminho do arquivo do banco.

    Usa o diretório de dados do usuário (XDG_DATA_HOME no Linux,
    AppData no Windows) para compatibilidade mobile.
    """
    data_dir = Path.home() / ".auth_app"
    data_dir.mkdir(parents=True, exist_ok=True)
    return str(data_dir / "auth.db")


class Database:
    """
    Gerencia a conexão e o ciclo de vida do banco SQLite.

    Expõe uma SessionFactory para criação de sessões.
    A arquitetura é preparada para criptografia futura
    (SQLCipher) apenas trocando a URL de conexão.
    """

    def __init__(self, db_path: str | None = None) -> None:
        path = db_path or _get_db_path()
        self._engine = create_engine(
            f"sqlite:///{path}",
            connect_args={"check_same_thread": False},
        )
        self._SessionFactory = sessionmaker(bind=self._engine)

    def create_tables(self) -> None:
        """Cria todas as tabelas definidas nos modelos ORM."""
        Base.metadata.create_all(self._engine)

    def get_session(self) -> Session:
        """Retorna uma nova sessão de banco."""
        return self._SessionFactory()

    def close(self) -> None:
        """Encerra a engine do banco."""
        self._engine.dispose()
