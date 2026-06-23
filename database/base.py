"""
Declaração da Base do SQLAlchemy.

Separada em módulo próprio para evitar importações circulares.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base para todos os modelos ORM."""
    pass
