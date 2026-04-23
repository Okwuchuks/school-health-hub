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
    QHBoxLayout,
    QListWidget,
    QStackedWidget,
)
from PySide6.QtCore import Signal


class DashBoard(QWidget):
    logout_requested = Signal()

    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self._init_ui()

    def _init_ui(self):
        outer_region = QHBoxLayout()

        self.side_panel = QWidget()

        self.main_content_area = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_content_area.setLayout(self.main_layout)

        self.upper_bar = QWidget()
        self.upper_bar.setLayout(QHBoxLayout())

        self.content_area = QStackedWidget()

        self.main_layout.addWidget(self.upper_bar)
        self.main_layout.addWidget(self.content_area)

        outer_region.addWidget(self.side_panel)
        outer_region.addWidget(self.main_content_area)

        self.setLayout(outer_region)

    def _handle_logout(self):
        QMessageBox.information(self, "Logged Out", "Successfully logged Out")
        self.logout_requested.emit()
