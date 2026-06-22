"""
Serviço de timer para atualização periódica dos códigos TOTP.

Encapsula o agendamento de chamadas periódicas usando o Clock do Kivy,
desacoplando o ViewModel da implementação concreta de scheduling.
"""

from typing import Callable, Optional

from kivy.clock import Clock, ClockEvent

from services.auth_service import AuthService


class TimerService:
    """
    Controla o ciclo de atualização periódica dos códigos TOTP.

    Usa o Clock do Kivy para agendar callbacks a cada segundo,
    delegando o cálculo do tempo restante ao AuthService — o
    TimerService não sabe nada sobre TOTP, apenas sobre "quando"
    disparar uma atualização.
    """

    def __init__(self, auth_service: AuthService) -> None:
        self._auth = auth_service
        self._event: Optional[ClockEvent] = None

    def start(self, callback: Callable[[], None]) -> None:
        """
        Inicia o timer, chamando `callback` a cada segundo.

        Se já existir um timer em execução, ele é cancelado antes
        de iniciar o novo (evita múltiplos agendamentos simultâneos).

        Args:
            callback: Função sem argumentos chamada a cada tick.
        """
        self.stop()
        self._event = Clock.schedule_interval(lambda dt: callback(), 1)

    def stop(self) -> None:
        """Cancela o agendamento atual, se existir."""
        if self._event is not None:
            self._event.cancel()
            self._event = None

    def seconds_remaining(self) -> int:
        """
        Retorna quantos segundos faltam até o próximo código TOTP.

        Returns:
            Inteiro de 0 a 29.
        """
        return self._auth.seconds_remaining()