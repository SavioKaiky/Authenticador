"""
Ponto de entrada da aplicação.

Este módulo deve permanecer extremamente simples.
Toda a lógica de inicialização pertence à classe AuthApplication.
"""

from core.application import AuthApplication


def main() -> None:
    """
    Inicializa a aplicação.
    """
    AuthApplication().run()


if __name__ == "__main__":
    main()