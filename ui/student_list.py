"""
School Health Hub (SHH)
The content area for the students section of the dashboard
Author: Ifende Daniel
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QComboBox,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)
from logic.calculations import calculate_grade


class StudentList(QWidget):
    def __init__(self, db_manager, user_data: tuple):
        super().__init__()
        self.db_manager = db_manager
        self.user_data = user_data
        self._init_ui()

    def _init_ui(self):
        main_area_layout = QVBoxLayout()

        self.top_bar = QWidget()
        self.top_bar_layout = QHBoxLayout()
        self.top_bar.setLayout(self.top_bar_layout)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search students by name or ID")

        self.filters_drop_down = QComboBox()

        self.add_student_button = QPushButton("➕ Add Student")

        self.delete_student_button = QPushButton("🗑️ Delete Student")

        if self.user_data[3] != "admin":
            self.delete_student_button.hide()

        self.top_bar_layout.addWidget(self.search_bar)
        self.top_bar_layout.addWidget(self.filters_drop_down)
        self.top_bar_layout.addWidget(self.add_student_button)
        self.top_bar_layout.addWidget(self.delete_student_button)

        self.student_area = QWidget()
        self._handle_student_info_area()

        main_area_layout.addWidget(self.top_bar)
        main_area_layout.addWidget(self.student_area)

        self.setLayout(main_area_layout)

    def _handle_student_info_area(self):
        student_layout = QVBoxLayout()

        students = self.db_manager.get_all_students()

        if students:
            table = QTableWidget()
            table.setRowCount(len(students))
            table.setColumnCount(8)
            table.setHorizontalHeaderLabels(
                ["Student ID", "Name", "Grade", "Date of Birth", "Gender", "Parent/Guardian", "Status", "Actions"]
            )

            activity = {1: "Active", 0: "Inactive"}

            for row, student in enumerate(students):
                full_name = f"{student[1]} {student[2] or ''} {student[3]}".strip()

                activities_combo = QComboBox()
                activities_combo.addItems(
                    ["View Student Info", "Edit Student", "Delete Student"]
                    if self.user_data[3] == "admin"
                    else ["View Student Info"]
                )

                table.setItem(row, 0, QTableWidgetItem(str(student[0])))
                table.setItem(row, 1, QTableWidgetItem(full_name))
                table.setItem(row, 2, QTableWidgetItem(str(calculate_grade(student[5]))))
                table.setItem(row, 3, QTableWidgetItem(str(student[4])))
                table.setItem(row, 4, QTableWidgetItem(str(student[7])))
                table.setItem(row, 5, QTableWidgetItem(str(student[9])))
                table.setItem(row, 6, QTableWidgetItem(activity.get(student[11])))
                table.setCellWidget(row, 7, activities_combo)

            student_layout.addWidget(table)

        else:
            student_layout.addWidget(QLabel("Currently no students"))

        self.student_area.setLayout(student_layout)
