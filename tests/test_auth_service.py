"""
Testes unitários do AuthService.

Não dependem de banco, UI ou Kivy — testam apenas a lógica
de geração e validação TOTP usando PyOTP diretamente.
"""

import time
import pyotp
import pytest

from services.auth_service import AuthService


@pytest.fixture
def service() -> AuthService:
    return AuthService()


# -------------------------------------------------------------------
# Chave de teste padrão RFC 6238 — amplamente usada como referência
# -------------------------------------------------------------------
VALID_SECRET = "JBSWY3DPEHPK3PXP"


class TestGenerateCode:

    def test_retorna_string_de_6_digitos(self, service):
        code = service.generate_code(VALID_SECRET)
        assert isinstance(code, str)
        assert len(code) == 6
        assert code.isdigit()

    def test_codigo_bate_com_pyotp_direto(self, service):
        """Garante que o AuthService gera o mesmo código que o PyOTP."""
        expected = pyotp.TOTP(VALID_SECRET).now()
        assert service.generate_code(VALID_SECRET) == expected

    def test_codigos_consecutivos_no_mesmo_periodo_sao_iguais(self, service):
        """Dois códigos gerados no mesmo período de 30s devem ser iguais."""
        code1 = service.generate_code(VALID_SECRET)
        code2 = service.generate_code(VALID_SECRET)
        assert code1 == code2

    def test_secret_minusculo_e_normalizado(self, service):
        """Chave em minúsculas deve gerar o mesmo código que em maiúsculas."""
        code_upper = service.generate_code(VALID_SECRET.upper())
        code_lower = service.generate_code(VALID_SECRET.lower())
        assert code_upper == code_lower

    def test_secret_invalido_lanca_excecao(self, service):
        with pytest.raises(Exception):
            service.generate_code("CHAVE_INVALIDA_!!!")


class TestSecondsRemaining:

    def test_retorna_inteiro_entre_0_e_29(self, service):
        seconds = service.seconds_remaining()
        assert isinstance(seconds, int)
        assert 0 <= seconds <= 30

    def test_consistente_com_time(self, service):
        """Verifica que o cálculo bate com time.time()."""
        expected = 30 - int(time.time()) % 30
        assert service.seconds_remaining() == expected


class TestIsValidSecret:

    def test_chave_base32_valida(self, service):
        assert service.is_valid_secret(VALID_SECRET) is True

    def test_chave_com_espacos_e_valida(self, service):
        secret_com_espacos = "JBSWY3DP EHPK3PXP"
        assert service.is_valid_secret(secret_com_espacos) is True

    def test_chave_minuscula_e_valida(self, service):
        assert service.is_valid_secret(VALID_SECRET.lower()) is True

    def test_chave_vazia_e_invalida(self, service):
        assert service.is_valid_secret("") is False

    def test_chave_com_caracteres_especiais_e_invalida(self, service):
        assert service.is_valid_secret("CHAVE_INVALIDA_!!!") is False

    def test_chave_com_numeros_invalidos_e_invalida(self, service):
        assert service.is_valid_secret("00000000") is False