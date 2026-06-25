"""
School Health Hub (SHH)
The content area for the students section of the dashboard
Author: Ifende Daniel
"""

from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QMessageBox,
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
        self.search_bar.textChanged.connect(self._filter_students)

        self.filters_drop_down = QComboBox()
        self.filters_drop_down.addItems(["All Statuses", "Active", "Inactive"])
        self.filters_drop_down.currentIndexChanged.connect(self._filter_students)

        self.add_student_button = QPushButton("➕ Add Student")

        self.delete_student_button = QPushButton("🗑️ Delete Student")
        self.delete_student_button.clicked.connect(self._delete_selected_student)

        if self.user_data[3] != "admin":
            self.delete_student_button.hide()

        self.top_bar_layout.addWidget(self.search_bar)
        self.top_bar_layout.addWidget(self.filters_drop_down)
        self.top_bar_layout.addWidget(self.add_student_button)
        self.top_bar_layout.addWidget(self.delete_student_button)

        self.student_area = QWidget()
        self.student_layout = QVBoxLayout()
        self.student_area.setLayout(self.student_layout)

        self.table = QTableWidget()
        self.empty_label = QLabel("Currently no students")

        self.student_layout.addWidget(self.table)
        self.student_layout.addWidget(self.empty_label)

        self.refresh_data()

        main_area_layout.addWidget(self.top_bar)
        main_area_layout.addWidget(self.student_area)

        self.setLayout(main_area_layout)

    def refresh_data(self):
        """Clears old data rows, re-queries database records, and handles the display state safely."""
        self.table.clear()

        students = self.db_manager.get_all_students()

        if students:
            self.empty_label.hide()
            self.table.show()

            self.table.setRowCount(len(students))
            self.table.setColumnCount(8)
            self.table.setHorizontalHeaderLabels(
                ["Student ID", "Name", "Grade", "Date of Birth", "Gender", "Parent/Guardian", "Status", "Actions"]
            )

            activity = {1: "Active", 0: "Inactive"}

            for row, student in enumerate(students):
                full_name = f"{student['first_name']} {student['middle_name'] or ''} {student['last_name']}".strip()

                activities_combo = QComboBox()
                activities_combo.addItems(
                    ["Select Action...", "View Student Info", "Edit Student", "Delete Student"]
                    if self.user_data[3] == "admin"
                    else ["View Student Info"]
                )

                self.table.setItem(row, 0, QTableWidgetItem(str(student["student_id"])))
                self.table.setItem(row, 1, QTableWidgetItem(full_name))
                self.table.setItem(row, 2, QTableWidgetItem(str(calculate_grade(student["enrollment_year"]))))
                self.table.setItem(row, 3, QTableWidgetItem(str(student["date_of_birth"])))
                self.table.setItem(row, 4, QTableWidgetItem(str(student["gender"])))
                self.table.setItem(row, 5, QTableWidgetItem(str(student["emergency_contact_name"])))
                self.table.setItem(row, 6, QTableWidgetItem(activity.get(student["is_active"])))
                self.table.setCellWidget(row, 7, activities_combo)
        else:
            self.table.hide()
            self.empty_label.show()

        self._filter_students()

    def _filter_students(self):
        """Processes live table searches and status constraints instantly on the client side."""
        if not hasattr(self, "table") or self.table.isHidden():
            return

        search_query = self.search_bar.text().lower().strip()
        selected_status = self.filters_drop_down.currentText()

        for row in range(self.table.rowCount()):
            id_item = self.table.item(row, 0)
            name_item = self.table.item(row, 1)
            status_item = self.table.item(row, 6)

            id_text = id_item.text().lower() if id_item else ""
            name_text = name_item.text().lower() if name_item else ""
            status_text = status_item.text() if status_item else ""

            matches_search = (search_query in id_text) or (search_query in name_text)

            matches_status = True
            if selected_status == "Active":
                matches_status = status_text == "Active"
            elif selected_status == "Inactive":
                matches_status = status_text == "Inactive"

            should_hide = not (matches_search and matches_status)
            self.table.setRowHidden(row, should_hide)

    def _delete_selected_student(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.information(self, "No Selected Student", "Please select a student to continue...")
            return

        student_id = self.table.item(selected_row, 0).text()
        student_name = self.table.item(selected_row, 1).text()

        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to completely remove Student: {student_name} ID: {student_id}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.db_manager.delete_student(student_id)
            self.refresh_data()
