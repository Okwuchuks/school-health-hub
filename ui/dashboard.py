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
    QStackedWidget,
    QComboBox,
)
from PySide6.QtCore import Signal, Qt


class DashBoard(QWidget):
    logout_requested = Signal()

    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.is_panel_expanded = True
        self._init_ui()

    def _init_ui(self):
        outer_region = QHBoxLayout()

        self.side_panel = QWidget()
        self.side_panel_layout = QVBoxLayout()
        self.side_panel.setLayout(self.side_panel_layout)

        self.patients_button = QPushButton("❤️‍🩹 Patients")
        self.records_button = QPushButton("🧾 Records")

        self.side_panel_layout.addWidget(
            self.patients_button, alignment=Qt.AlignmentFlag.AlignTop
        )
        self.side_panel_layout.addWidget(
            self.records_button, alignment=Qt.AlignmentFlag.AlignTop
        )

        self.main_content_area = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_content_area.setLayout(self.main_layout)

        self.upper_bar = QWidget()
        self.upper_bar_layout = QHBoxLayout()
        self.upper_bar.setLayout(self.upper_bar_layout)

        self.avatar_label = QLabel("ID")

        self.settings_combobox = QComboBox()
        self.settings_combobox.addItems(["Profile", "Settings", "Logout"])
        self.settings_combobox.currentTextChanged.connect(
            self._check_if_logout
        )

        toggle_button = QPushButton("☰")
        toggle_button.clicked.connect(self._toggle_side_panel)

        self.upper_bar_layout.addWidget(
            toggle_button, alignment=Qt.AlignmentFlag.AlignLeft
        )

        self.upper_bar_layout.addWidget(
            self.avatar_label, alignment=Qt.AlignmentFlag.AlignRight
        )

        self.upper_bar_layout.addWidget(
            self.settings_combobox, alignment=Qt.AlignmentFlag.AlignRight
        )

        self.content_area = QStackedWidget()

        self.main_layout.addWidget(self.upper_bar)
        self.main_layout.addWidget(self.content_area)

        outer_region.addWidget(self.side_panel)
        outer_region.addWidget(self.main_content_area)

        self.setLayout(outer_region)

    def _handle_logout(self):
        QMessageBox.information(self, "Logged Out", "Successfully logged Out")
        self.logout_requested.emit()

    def _check_if_logout(self, text: str):
        if text == "Logout":
            self._handle_logout()

    def _toggle_side_panel(self):
        if self.is_panel_expanded:
            self.side_panel.setFixedWidth(60)
            self.patients_button.setText("❤️‍🩹")
            self.records_button.setText("🧾")

        else:
            self.side_panel.setFixedWidth(200)
            self.patients_button.setText("❤️‍🩹 Patients")
            self.records_button.setText("🧾 Records")

        self.is_panel_expanded = not self.is_panel_expanded
