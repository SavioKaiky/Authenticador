"""
Ponto de entrada da aplicação.

Este arquivo deve permanecer o mais simples possível.
Toda a lógica de inicialização pertence ao módulo core.
"""

from core.application import AuthApplication


def main() -> None:
    """Inicializa e executa a aplicação."""
    AuthApplication().run()


if __name__ == "__main__":
    main()