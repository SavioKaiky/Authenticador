"""
Modelo ORM para a tabela de contas.

Separado dos modelos de domínio para não misturar
SQLAlchemy com lógica de negócio.
"""

from datetime import datetime, timezone

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class AccountORM(Base):
    """
    Representação ORM da tabela 'accounts'.

    A coluna 'secret' armazena a chave Base32.
    Em versão futura, será criptografada com AES-256 antes
    de ser persistida.
    """

    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    secret: Mapped[str] = mapped_column(String(256), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )