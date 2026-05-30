"""
School Health Hub (SHH)
The landing page(The Dashboard)
Author: Ifende Daniel
"""

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from ui.staff_list import StaffList
from ui.staff_patient_form import StaffPatientForm
from ui.student_list import StudentList
from ui.student_patient_form import StudentPatientForm


class DashBoard(QWidget):
    logout_requested = Signal()

    def __init__(self, db_manager, user_data: tuple):
        super().__init__()
        self.db_manager = db_manager
        self.user_data = user_data
        self.is_panel_expanded = True
        self._init_ui()

    def _init_ui(self):
        first_name = self.user_data[4]
        last_name = self.user_data[5]
        user_name = self.user_data[1]
        user_type = self.user_data[3]

        outer_region = QHBoxLayout()

        self.side_panel = QWidget()
        self.side_panel_layout = QVBoxLayout()
        self.side_panel.setLayout(self.side_panel_layout)

        self.home_button = QPushButton("🏠 Home")
        self.home_button.setCheckable(True)

        self.patients_button = QPushButton("❤️‍🩹 Patients")
        self.patients_button.setCheckable(True)

        self.staff_button = QPushButton("👥 Staff")
        self.staff_button.setCheckable(True)
        self.staff_button.clicked.connect(self._switch_to_staff_list)

        self.student_button = QPushButton("🎓 Students")
        self.student_button.setCheckable(True)
        self.student_button.clicked.connect(self._switch_to_student_list)

        self.visits_button = QPushButton("🎫 Visits")
        self.visits_button.setCheckable(True)

        self.analytics_button = QPushButton("📊 Analytics")
        self.analytics_button.setCheckable(True)

        self.side_panel_layout.addWidget(self.home_button, alignment=Qt.AlignmentFlag.AlignTop)
        self.side_panel_layout.addWidget(self.patients_button, alignment=Qt.AlignmentFlag.AlignTop)
        self.side_panel_layout.addWidget(self.staff_button, alignment=Qt.AlignmentFlag.AlignTop)
        self.side_panel_layout.addWidget(self.student_button, alignment=Qt.AlignmentFlag.AlignTop)
        self.side_panel_layout.addWidget(self.visits_button, alignment=Qt.AlignmentFlag.AlignTop)
        self.side_panel_layout.addWidget(self.analytics_button, alignment=Qt.AlignmentFlag.AlignTop)

        self.main_content_area = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_content_area.setLayout(self.main_layout)

        self.upper_bar = QWidget()
        self.upper_bar_layout = QHBoxLayout()
        self.upper_bar.setLayout(self.upper_bar_layout)

        self.avatar_label = QLabel(f"{first_name[0]} {last_name[0]}")

        self.settings_combobox = QComboBox()
        self.settings_combobox.addItems(["Profile", "Settings", "Logout"])
        self.settings_combobox.currentTextChanged.connect(self._check_if_logout)

        toggle_button = QPushButton("☰")
        toggle_button.clicked.connect(self._toggle_side_panel)

        self.upper_bar_layout.addWidget(toggle_button, alignment=Qt.AlignmentFlag.AlignLeft)

        self.upper_bar_layout.addWidget(self.avatar_label, alignment=Qt.AlignmentFlag.AlignRight)

        self.upper_bar_layout.addWidget(self.settings_combobox, alignment=Qt.AlignmentFlag.AlignRight)

        self.content_area = QStackedWidget()

        self.student_list = StudentList(self.db_manager, self.user_data)
        self.student_list.add_student_button.clicked.connect(self._switch_to_add_student_form)

        self.student_patient_form = StudentPatientForm(self.db_manager)
        self.student_patient_form.back_button.clicked.connect(self._switch_to_student_list)

        self.staff_list = StaffList(self.db_manager, self.user_data)
        self.staff_list.add_staff_button.clicked.connect(self._switch_to_add_staff_form)

        self.staff_patient_form = StaffPatientForm(self.db_manager)
        self.staff_patient_form.back_button.clicked.connect(self._switch_to_staff_list)

        self.content_area.addWidget(self.student_list)
        self.content_area.addWidget(self.student_patient_form)
        self.content_area.addWidget(self.staff_list)
        self.content_area.addWidget(self.staff_patient_form)

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
            self.home_button.setText("🏠")
            self.patients_button.setText("❤️‍🩹")
            self.staff_button.setText("👥")
            self.student_button.setText("🎓")
            self.visits_button.setText("🎫")
            self.analytics_button.setText("📊")
        else:
            self.side_panel.setFixedWidth(160)
            self.home_button.setText("🏠 Home")
            self.patients_button.setText("❤️‍🩹 Patients")
            self.staff_button.setText("👥 Staff")
            self.student_button.setText("🎓 Students")
            self.visits_button.setText("🎫 Visits")
            self.analytics_button.setText("📊 Analytics")

        self.is_panel_expanded = not self.is_panel_expanded

    def _switch_to_student_list(self):
        self.content_area.setCurrentWidget(self.student_list)

    def _switch_to_add_student_form(self):
        self.content_area.setCurrentWidget(self.student_patient_form)

    def _switch_to_staff_list(self):
        self.content_area.setCurrentWidget(self.staff_list)

    def _switch_to_add_staff_form(self):
        self.content_area.setCurrentWidget(self.staff_patient_form)
