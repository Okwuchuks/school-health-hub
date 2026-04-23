"""
School Health Hub (SHH)
The registration window
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
from security.auth import register_user


class RegistrationScreen(QWidget):
    registration_success = Signal()

    def __init__(self, db_manager, user_type):
        super().__init__()
        self.db_manager = db_manager
        self.user_type = user_type
        self._init_ui()

    def _init_ui(self):
        title_label = QLabel("School Health Hub - Register")

        input_field = QFormLayout()

        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText(
            "Insert your firstname here..."
        )
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Insert your lastname here...")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Insert your username here...")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Insert your password here...")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Insert your phone number here...")

        self.conf_password = QLineEdit()
        self.conf_password.setPlaceholderText("Pls confirm your password...")
        self.conf_password.setEchoMode(QLineEdit.EchoMode.Password)

        input_field.addRow("First name:", self.first_name_input)
        input_field.addRow("Last name:", self.last_name_input)
        input_field.addRow("Username:", self.username_input)
        input_field.addRow("Password:", self.password_input)
        input_field.addRow("Confirm Password", self.conf_password)
        input_field.addRow("Phone no.:", self.phone_input)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self._handle_register)

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addLayout(input_field)
        layout.addWidget(register_button)

        self.setLayout(layout)

    def _handle_register(self):
        username = self.username_input.text()
        firstname = self.first_name_input.text()
        lastname = self.last_name_input.text()
        password = self.password_input.text()
        password_conf = self.conf_password.text()
        phone_no = self.phone_input.text()

        if (
            not username
            or not firstname
            or not lastname
            or not password
            or not phone_no
        ):
            QMessageBox.warning(self, "Error", "Please fill in all fields")
            return

        if password_conf != password:
            QMessageBox.information(
                self,
                "Confirm Password",
                "Please confirm your password correctly",
            )
            return

        register_user(
            self.db_manager,
            username,
            password,
            self.user_type,
            firstname,
            lastname,
            phone_no,
        )

        QMessageBox.information(
            self, "Success", "Account successfully created"
        )
        self.registration_success.emit()
