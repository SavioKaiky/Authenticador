"""
Configuração e inicialização do banco de dados SQLite.
"""
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from database.base import Base

def _get_db_path() -> str:
    """
    Retorna o caminho do arquivo do banco.
    No Android usa o diretório privado do app.
    No desktop usa ~/.auth_app/.
    """
    # Android: ANDROID_PRIVATE aponta para /data/user/0/<pkg>/files
    android_private = os.environ.get("ANDROID_PRIVATE")
    if android_private:
        data_dir = Path(android_private) / "auth_app"
    else:
        data_dir = Path.home() / ".auth_app"

    data_dir.mkdir(parents=True, exist_ok=True)
    return str(data_dir / "auth.db")

class Database:
    def __init__(self, db_path: str | None = None) -> None:
        path = db_path or _get_db_path()
        self._engine = create_engine(
            f"sqlite:///{path}",
            connect_args={"check_same_thread": False},
        )
        self._SessionFactory = sessionmaker(bind=self._engine)

    def create_tables(self) -> None:
        Base.metadata.create_all(self._engine)

    def get_session(self) -> Session:
        return self._SessionFactory()

    def close(self) -> None:
        self._engine.dispose()
