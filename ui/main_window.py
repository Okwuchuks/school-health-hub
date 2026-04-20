"""
School Health Hub (SHH)
Main Window Layout
Author: Ifende Daniel
"""

from PySide6.QtWidgets import QMainWindow, QStackedWidget
from ui.login_screen import LoginScreen
from ui.registration_screen import RegistrationScreen
from database.db_manager import DatabaseManager
from security.auth import is_first_run


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager("school_health_record.db")
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("School Health Hub")

        self.showMaximized()

        self.container = QStackedWidget()
        self.setCentralWidget(self.container)

        self.login_screen = LoginScreen(self.db_manager)

        if is_first_run(self.db_manager):
            self.registration_screen = RegistrationScreen(
                self.db_manager, "admin"
            )
        else:
            self.registration_screen = RegistrationScreen(
                self.db_manager, "user"
            )

        self.container.addWidget(self.login_screen)
        self.container.addWidget(self.registration_screen)

        self.registration_screen.registration_success.connect(
            self._switch_to_login
        )
        self.login_screen.login_success.connect(self._switch_to_dashboard)

        if is_first_run(self.db_manager):
            self.container.setCurrentWidget(self.registration_screen)
        else:
            self.container.setCurrentWidget(self.login_screen)

    def _switch_to_login(self):
        self.container.setCurrentWidget(self.login_screen)

    def _switch_to_dashboard(self):
        print("successfully switched to dashboard")
