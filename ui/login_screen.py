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
    QRadioButton,
    QHBoxLayout,
    QButtonGroup,
)
from security.auth import verify_login, is_first_run, register_user


# -----LOGIN SCREEN VIEW...
class LoginScreen(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self._init_ui()

    def _init_ui(self):
        if is_first_run(self.db_manager):
            self._build_register_form()
        else:
            self._build_login_form()

    def _build_login_form(self):
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

        layout.addWidget(title_label)
        layout.addLayout(input_field)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def _build_register_form(self):
        title_label = QLabel("School Health Hub - Register")

        input_field = QFormLayout()

        self.full_name_input = QLineEdit()
        self.full_name_input.setPlaceholderText("Insert your fullname here...")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Insert your username here...")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Insert your password here...")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Insert your phone number here...")

        input_field.addRow("Full name:", self.full_name_input)
        input_field.addRow("Username:", self.username_input)
        input_field.addRow("Password:", self.password_input)
        input_field.addRow("Phone no.:", self.phone_input)

        gender_field = QHBoxLayout()
        gender_label = QLabel("Gender:")

        self.male_input = QRadioButton("Male")
        self.female_input = QRadioButton("Female")

        self.gender_group = QButtonGroup()
        self.gender_group.addButton(self.male_input)
        self.gender_group.addButton(self.female_input)

        gender_field.addWidget(gender_label)
        gender_field.addWidget(self.male_input)
        gender_field.addWidget(self.female_input)

        blood_group_label = QLabel("Blood Group:")

        self.A_pos = QRadioButton("A+")
        self.A_neg = QRadioButton("A-")
        self.B_pos = QRadioButton("B+")
        self.B_neg = QRadioButton("B-")
        self.O_pos = QRadioButton("O+")
        self.O_neg = QRadioButton("O-")
        self.AB_pos = QRadioButton("AB+")
        self.AB_neg = QRadioButton("AB-")

        row_1 = QHBoxLayout()
        for widget in [self.A_neg, self.A_pos, self.B_neg, self.B_pos]:
            row_1.addWidget(widget)

        row_2 = QHBoxLayout()
        for widget in [self.O_neg, self.O_pos, self.AB_neg, self.AB_pos]:
            row_2.addWidget(widget)

        self.blood_group_buttons = QButtonGroup()
        self.blood_group_buttons.addButton(self.A_pos)
        self.blood_group_buttons.addButton(self.A_neg)
        self.blood_group_buttons.addButton(self.B_pos)
        self.blood_group_buttons.addButton(self.B_neg)
        self.blood_group_buttons.addButton(self.O_pos)
        self.blood_group_buttons.addButton(self.O_neg)
        self.blood_group_buttons.addButton(self.AB_pos)
        self.blood_group_buttons.addButton(self.AB_neg)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self._handle_register)

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addLayout(input_field)
        layout.addLayout(gender_field)
        layout.addWidget(blood_group_label)
        layout.addLayout(row_1)
        layout.addLayout(row_2)
        layout.addWidget(register_button)

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
            QMessageBox.warning(
                self, "Login Failed", "Invalid username or password"
            )

    def _clear_layout(self):
        if self.layout():
            while self.layout().count():
                item = self.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
        QWidget().setLayout(self.layout())

    def _handle_register(self):
        username = self.username_input.text()
        fullname = self.full_name_input.text()
        password = self.password_input.text()
        phone_no = self.phone_input.text()

        if self.male_input.isChecked():
            gender = "Male"
        else:
            gender = "Female"

        if self.A_neg.isChecked():
            b_group = "A-"
        elif self.A_pos.isChecked():
            b_group = "A+"
        elif self.AB_neg.isChecked():
            b_group = "AB-"
        elif self.AB_pos.isChecked():
            b_group = "AB+"
        elif self.B_neg.isChecked():
            b_group = "B-"
        elif self.B_pos.isChecked():
            b_group = "B+"
        elif self.O_neg.isChecked():
            b_group = "O-"
        else:
            b_group = "O+"

        if (
            not username
            or not fullname
            or not password
            or not phone_no
            or not gender
            or not b_group
        ):
            QMessageBox.warning(self, "Error", "Please fill in all fields")
            return

        register_user(
            self.db_manager,
            username,
            password,
            "admin",
            fullname,
            phone_no,
            gender,
            b_group,
        )

        QMessageBox.information(
            self, "Success", "Admin account successfully created"
        )

        self._clear_layout()

