"""
Classe principal da aplicação.

Responsável por:
- Inicializar o banco de dados
- Registrar dependências no container
- Configurar o roteador de telas
- Configurar o tema
"""

import os
import sys

# Garante que o diretório raiz do projeto está no path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kivymd.app import MDApp

from core.dependency_container import DependencyContainer
from core.lifecycle import ApplicationLifecycle
from core.router import AppRouter
from core.settings import APP_NAME

from database.database import Database
from database.migrations import initialize_database
from database.session import AccountORM
from database.repositories.account_repository import AccountRepository

from services.auth_service import AuthService
from services.account_service import AccountService
from services.timer_service import TimerService

from viewmodels.home_viewmodel import HomeViewModel
from viewmodels.add_account_viewmodel import AddAccountViewModel

from ui.theme import ThemeManager


class AuthApplication(MDApp):
    """Ponto de entrada e compositor da aplicação."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.container = DependencyContainer()
        self.router = AppRouter()
        self.lifecycle = ApplicationLifecycle()
        self._db: Database | None = None

    def build(self):
        self.title = APP_NAME
        ThemeManager.configure(self)
        self._setup_database()
        self._setup_services()
        self._setup_screens()
        return self.router.manager

    def _setup_database(self) -> None:
        """Inicializa o banco e executa migrações."""
        self._db = Database()
        initialize_database(self._db)

    def _setup_services(self) -> None:
        """Registra serviços e viewmodels no container."""
        session = self._db.get_session()
        repository = AccountRepository(session)
        auth_service = AuthService()
        account_service = AccountService(repository, auth_service)
        timer_service = TimerService(auth_service)

        self.container.register_singleton("account_service", account_service)
        self.container.register_singleton("auth_service", auth_service)
        self.container.register_singleton("timer_service", timer_service)

        home_vm = HomeViewModel(account_service, timer_service)
        add_vm = AddAccountViewModel(account_service)
        self.container.register_singleton("home_viewmodel", home_vm)
        self.container.register_singleton("add_account_viewmodel", add_vm)

    def _setup_screens(self) -> None:
        """Registra as telas no roteador."""
        from ui.screens.splash_screen import SplashScreen
        from ui.screens.home_screen import HomeScreen
        from ui.screens.add_account_screen import AddAccountScreen

        self.router.register(SplashScreen(name="splash"))
        self.router.register(HomeScreen(name="home"))
        self.router.register(AddAccountScreen(name="add_account"))
        self.router.navigate("home")

    def on_start(self):
        self.lifecycle.on_start()

    def on_pause(self):
        return self.lifecycle.on_pause()

    def on_resume(self):
        self.lifecycle.on_resume()

    def on_stop(self):
        if self._db:
            self._db.close()
        self.lifecycle.on_stop()
