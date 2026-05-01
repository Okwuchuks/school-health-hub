"""
School Health Hub (SHH)
The form which is used to add student patients
Author: Ifende Daniel
"""

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QVBoxLayout,
    QPushButton,
    QDateEdit,
    QMessageBox,
)
from PySide6.QtCore import Signal, Qt, QDate
import datetime


class PatientForm(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout()

        form_space = QWidget()
        form_layout = QHBoxLayout()
        form_space.setLayout(form_layout)

        left_form = QWidget()
        left_form_layout = QFormLayout()
        left_form.setLayout(left_form_layout)

        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("Insert first name here...")

        self.middle_name = QLineEdit()
        self.middle_name.setPlaceholderText("Insert middle name here... (not compulsory)")

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Insert last name here...")

        self.birthday = QDateEdit()
        self.birthday.setCalendarPopup(True)

        cur_year = datetime.date.today().year

        self.birthday.setMinimumDate(QDate((cur_year - 10), 1, 1))
        self.birthday.setMaximumDate(QDate((cur_year - 3), 12, 31))

        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female"])

        left_form_layout.addRow("First Name:", self.first_name)
        left_form_layout.addRow("Middle Name:", self.middle_name)
        left_form_layout.addRow("Last Name:", self.last_name)
        left_form_layout.addRow("Date Of Birth:", self.birthday)
        left_form_layout.addRow("Gender:", self.gender)

        right_form = QWidget()
        right_form_layout = QFormLayout()
        right_form.setLayout(right_form_layout)

        self.enrollment_year = QLineEdit()
        self.enrollment_year.setPlaceholderText("Insert the year of the enrolled student...")

        self.blood_group = QComboBox()
        self.blood_group.addItems(["A-", "A+", "B-", "B+", "O-", "O+", "AB+", "AB-"])

        self.hostel = QComboBox()

        self.emerg_cont_name = QLineEdit()
        self.emerg_cont_name.setPlaceholderText("Insert the emergency contact name here...")

        self.emerg_cont_num = QLineEdit()
        self.emerg_cont_num.setPlaceholderText("Insert the emergency contact number here...")

        right_form_layout.addRow("Enrollment Year:", self.enrollment_year)
        right_form_layout.addRow("Blood Group:", self.blood_group)
        right_form_layout.addRow("Hostel:", self.hostel)
        right_form_layout.addRow("Emergency Contact:", self.emerg_cont_num)
        right_form_layout.addRow("Emergency Contact Name:", self.emerg_cont_name)

        form_layout.addWidget(left_form)
        form_layout.addWidget(right_form)

        button_space = QWidget()
        button_layout = QHBoxLayout()
        button_space.setLayout(button_layout)

        self.add_user_button = QPushButton("Add Student")
        self.add_user_button.clicked.connect(self._add_student)

        self.back_button = QPushButton("Back")

        button_layout.addWidget(self.add_user_button)
        button_layout.addWidget(self.back_button)

        main_layout.addWidget(form_space)
        main_layout.addWidget(button_space)

        self.setLayout(main_layout)

    def _add_student(self):
        """
        [It adds a student to the database]
        """

        middle_name = self.middle_name.text().strip()

        info = {
            "Firstname": self.first_name.text().strip(),
            "Lastname": self.last_name.text().strip(),
            "Birthday": self.birthday.date().toString("yyyy-MM-dd"),
            "Gender": self.gender.currentText(),
            "Enrollment Year": self.enrollment_year.text().strip(),
            "Blood Group": self.blood_group.currentText(),
            "Hostel": self.hostel.currentText(),
            "Emergency Contact": self.emerg_cont_num.text().strip(),
            "Emergency Contact Name": self.emerg_cont_name.text().strip(),
        }

        empty_fields = []

        for name, data in info.items():
            if not data:
                empty_fields.append(name)

        if empty_fields:
            QMessageBox.information(self, "Empty Input", "Please fill all required fields" )
            return
        else:
            pass
