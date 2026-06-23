"""
Modelo de domínio para uma conta 2FA.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Account:
    """
    Representa uma conta cadastrada no autenticador.

    Attributes:
        name: Nome de exibição da conta (ex: Google, GitHub).
        secret: Chave secreta TOTP em Base32.
        id: Identificador único gerado automaticamente.
        created_at: Data de criação do registro.
    """

    name: str
    secret: str
    id: int | None = field(default=None)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        self.secret = self.secret.strip().upper().replace(" ", "")
