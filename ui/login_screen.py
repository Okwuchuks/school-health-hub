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


# -----LOGIN SCREEN VIEW...
class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
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

        layout = QVBoxLayout()

        layout.addWidget(title_label)
        layout.addLayout(input_field)
        layout.addWidget(login_button)

        self.setLayout(layout)

        # the logic of adding a first user will come here later
