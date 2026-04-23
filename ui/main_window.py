"""
School Health Hub (SHH)
Main Window Layout
Author: Ifende Daniel
"""

from PySide6.QtWidgets import QMainWindow, QStackedWidget
from ui.login_screen import LoginScreen
from ui.registration_screen import RegistrationScreen
from ui.dashboard import DashBoard
from database.db_manager import DatabaseManager
from security.auth import is_first_run


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager("school_health_record.db")
        self.is_first_run = is_first_run(self.db_manager)
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("School Health Hub")

        self.showMaximized()

        self.container = QStackedWidget()
        self.setCentralWidget(self.container)

        self.login_screen = LoginScreen(self.db_manager)
        self.dashboard = DashBoard(self.db_manager)

        if self.is_first_run:
            self.registration_screen = RegistrationScreen(
                self.db_manager, "admin"
            )
        else:
            self.registration_screen = RegistrationScreen(
                self.db_manager, "user"
            )

        self.container.addWidget(self.login_screen)
        self.container.addWidget(self.registration_screen)
        self.container.addWidget(self.dashboard)

        self.registration_screen.registration_success.connect(
            self._switch_to_login
        )
        self.login_screen.login_success.connect(self._switch_to_dashboard)
        self.dashboard.logout_requested.connect(self._switch_to_login)

        if self.is_first_run:
            self.container.setCurrentWidget(self.registration_screen)
        else:
            self.container.setCurrentWidget(self.login_screen)

    def _switch_to_login(self):
        self.container.setCurrentWidget(self.login_screen)
        self.login_screen.clear_input_fields()

    def _switch_to_dashboard(self):
        self.container.setCurrentWidget(self.dashboard)
