"""
Serviço de geração de códigos TOTP.

Encapsula toda interação com a biblioteca PyOTP.
A lógica de negócio fica aqui; a UI nunca toca PyOTP diretamente.
"""

import time
import pyotp


TOTP_PERIOD = 30  # segundos padrão RFC 6238


class AuthService:
    """
    Gera e valida códigos TOTP (Time-based One-Time Password).
    """

    def generate_code(self, secret: str) -> str:
        """
        Gera o código TOTP atual de 6 dígitos.

        Args:
            secret: Chave secreta Base32 da conta.

        Returns:
            Código de 6 dígitos como string (ex: "123456").

        Raises:
            ValueError: Se a chave secreta for inválida.
        """
        totp = pyotp.TOTP(secret)
        return totp.now()

    def seconds_remaining(self) -> int:
        """
        Retorna quantos segundos faltam até o próximo código.

        Returns:
            Inteiro de 0 a 29.
        """
        return TOTP_PERIOD - int(time.time()) % TOTP_PERIOD

    def is_valid_secret(self, secret: str) -> bool:
        """
        Valida se uma chave Base32 é utilizável.

        O PyOTP aceita string vazia sem lançar exceção — por isso
        verificamos explicitamente se a chave está vazia após a
        normalização, antes de tentar gerar o código.

        Args:
            secret: Chave a validar.

        Returns:
            True se válida.
        """
        try:
            cleaned = secret.strip().upper().replace(" ", "")
            if not cleaned:
                return False
            pyotp.TOTP(cleaned).now()
            return True
        except Exception:
            return False