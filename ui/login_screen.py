"""
School Health Hub (SHH)
The login window
Author: Ifende Daniel
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QMessageBox,
    QLineEdit,
    QFormLayout,
)
from PySide6.QtCore import Signal
from security.auth import verify_login


# -----LOGIN SCREEN VIEW...
class LoginScreen(QWidget):
    login_success = Signal()

    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self._init_ui()

    def _init_ui(self):
        title_label = QLabel("School Health Hub - Login")

        input_field = QFormLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Insert your username here...")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Insert your password here...")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        input_field.addRow("User Name:", self.username_input)
        input_field.addRow("Password:", self.password_input)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self._handle_login)

        layout = QVBoxLayout()
        layout.setContentsMargins(64, 64, 64, 64)
        layout.setSpacing(32)

        layout.addWidget(title_label)
        layout.addLayout(input_field)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def clear_input_fields(self):
        self.username_input.clear()
        self.password_input.clear()

    def _handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please fill in all fields")
            return

        if verify_login(self.db_manager, username, password):
            self.login_success.emit()
        else:
            QMessageBox.warning(
                self, "Login Failed", "Invalid username or password"
            )
            self.clear_input_fields()
