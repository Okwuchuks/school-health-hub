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
from security.auth import verify_login


# -----LOGIN SCREEN VIEW...
class LoginScreen(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self._init_ui()

    def _init_ui(self):
        title_label = QLabel("School Health Hub")

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

        layout.addWidget(title_label)
        layout.addLayout(input_field)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def _handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please fill in all fields")
            return

        if verify_login(self.db_manager, username, password):
            pass
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")
