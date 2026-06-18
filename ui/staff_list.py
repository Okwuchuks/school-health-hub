"""
School Health Hub (SHH)
The content area for the staff section of the dashboard
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
)


class StaffList(QWidget):
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
        self.search_bar.setPlaceholderText("Search staff by name or ID")

        self.filters_drop_down = QComboBox()

        self.add_staff_button = QPushButton("➕ Add Staff")

        self.delete_staff_button = QPushButton("🗑️ Delete Staff")

        if self.user_data[3] != "admin":
            self.delete_staff_button.hide()

        self.top_bar_layout.addWidget(self.search_bar)
        self.top_bar_layout.addWidget(self.filters_drop_down)
        self.top_bar_layout.addWidget(self.add_staff_button)
        self.top_bar_layout.addWidget(self.delete_staff_button)

        self.staff_area = QWidget()
        self._handle_staff_info_area()

        main_area_layout.addWidget(self.top_bar)
        main_area_layout.addWidget(self.staff_area)

        self.setLayout(main_area_layout)

    def _handle_staff_info_area(self):
        staff_layout = QVBoxLayout()

        staff = self.db_manager.get_all_staff()

        if staff:
            table = QTableWidget()
            table.setRowCount(len(staff))
            table.setColumnCount(7)
            table.setHorizontalHeaderLabels(
                ["Staff ID", "Name", "Office", "Date of Birth", "Gender", "Status", "Actions"]
            )

            activity = {1: "Active", 0: "Inactive"}

            for row, staff in enumerate(staff):
                full_name = f"{staff[1]} {staff[2] or ''} {staff[3]}".strip()

                activities_combo = QComboBox()
                activities_combo.addItems(
                    ["View Staff Info", "Edit Staff", "Delete Staff"]
                    if self.user_data[3] == "admin"
                    else ["View Staff Info"]
                )

                table.setItem(row, 0, QTableWidgetItem(str(staff[0])))
                table.setItem(row, 1, QTableWidgetItem(full_name))
                table.setItem(row, 2, QTableWidgetItem(str(staff[4])))
                table.setItem(row, 3, QTableWidgetItem(str(staff[7])))
                table.setItem(row, 4, QTableWidgetItem(str(staff[9])))
                table.setItem(row, 5, QTableWidgetItem(activity.get(staff[11])))
                table.setCellWidget(row, 8, activities_combo)

            staff_layout.addWidget(table)

        else:
            staff_layout.addWidget(QLabel("Currently no staff"))

        self.staff_area.setLayout(staff_layout)
