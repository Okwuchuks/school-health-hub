"""
School Health Hub (SHH)
The layout for the main window
Author: Ifende Daniel
"""

from PySide6.QtWidgets import QStackedWidget, QMainWindow
from ui.login_screen import LoginScreen
from database.db_manager import DatabaseManager


# -----THE MAIN WINDOW CLASS..
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager("school_health_record.db")
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("School Health Hub")

        screen = self.screen().availableGeometry()
        x = screen.width()
        y = screen.height()

        self.resize(x, y)

        # Screens will be added here as the app grows
        self.container = QStackedWidget()

        self.login_screen = LoginScreen(self.db_manager)
        self.container.addWidget(self.login_screen)

        self.container.setCurrentIndex(0)
        self.setCentralWidget(self.container)
