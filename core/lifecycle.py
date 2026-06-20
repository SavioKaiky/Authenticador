"""
Gerenciamento do ciclo de vida da aplicação.

Centraliza eventos de inicialização e encerramento.
"""


class ApplicationLifecycle:
    """
    Responsável pelos eventos da aplicação.
    """

    def on_start(self):
        """
        Executado quando a aplicação inicia.
        """
        print(">> Auth App iniciado.")

    def on_pause(self):
        """
        Executado quando o aplicativo vai para segundo plano.

        Returns:
            bool
        """
        print(">> Aplicação pausada.")
        return True

    def on_resume(self):
        """
        Executado quando o aplicativo retorna.
        """
        print(">> Aplicação retomada.")

    def on_stop(self):
        """
        Executado ao encerrar a aplicação.
        """
        print(">> Auth App encerrado.")