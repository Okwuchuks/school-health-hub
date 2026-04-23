"""
School Health Hub (SHH)
The landing page(The Dashboard)
Author: Ifende Daniel
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QMessageBox,
)
from PySide6.QtCore import Signal


class DashBoard(QWidget):
    logout_requested = Signal()

    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self._init_ui()

    def _init_ui(self):
        title_label = QLabel("Welcome")

        logout_button = QPushButton("Logout")
        logout_button.clicked.connect(self._handle_logout)

        layout = QVBoxLayout()

        layout.addWidget(title_label)
        layout.addWidget(logout_button)

        self.setLayout(layout)

    def _handle_logout(self):
        QMessageBox.information(self, "Logged Out", "Successfully logged Out")
        self.logout_requested.emit()
