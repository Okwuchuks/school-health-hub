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
        self.search_bar.textChanged.connect(self._filter_staff)

        self.filters_drop_down = QComboBox()
        self.filters_drop_down.addItems(["All Statuses", "Active", "Inactive"])
        self.filters_drop_down.currentIndexChanged.connect(self._filter_staff)

        self.add_staff_button = QPushButton("➕ Add Staff")
        self.delete_staff_button = QPushButton("🗑️ Delete Staff")

        if self.user_data[3] != "admin":
            self.delete_student_button.hide()

        self.top_bar_layout.addWidget(self.search_bar)
        self.top_bar_layout.addWidget(self.filters_drop_down)
        self.top_bar_layout.addWidget(self.add_staff_button)
        self.top_bar_layout.addWidget(self.delete_staff_button)

        self.staff_area = QWidget()
        self.staff_layout = QVBoxLayout()
        self.staff_area.setLayout(self.staff_layout)

        self.table = QTableWidget()
        self.empty_label = QLabel("Currently no staff members")

        self.staff_layout.addWidget(self.table)
        self.staff_layout.addWidget(self.empty_label)

        self.refresh_data()

        main_area_layout.addWidget(self.top_bar)
        main_area_layout.addWidget(self.staff_area)

        self.setLayout(main_area_layout)

    def refresh_data(self):
        """Clears old rows, re-queries database staff records, and populates the view layout safely."""
        self.table.clear()

        staff_members = self.db_manager.get_all_staff()

        if staff_members:
            self.empty_label.hide()
            self.table.show()

            self.table.setRowCount(len(staff_members))
            self.table.setColumnCount(8)
            self.table.setHorizontalHeaderLabels(
                ["Staff ID", "Name", "Role", "Date of Birth", "Gender", "Office/Department", "Status", "Actions"]
            )

            activity = {1: "Active", 0: "Inactive"}

            for row, staff in enumerate(staff_members):
                full_name = f"{staff['first_name']} {staff['middle_name'] or ''} {staff['last_name']}".strip()

                actions_combo = QComboBox()
                actions_combo.addItems(
                    ["View Staff Info", "Edit Staff", "Delete Staff"]
                    if self.user_data[3] == "admin"
                    else ["View Staff Info"]
                )

                self.table.setItem(row, 0, QTableWidgetItem(str(staff["staff_id"])))
                self.table.setItem(row, 1, QTableWidgetItem(full_name))
                self.table.setItem(row, 2, QTableWidgetItem(str(staff["role"])))
                self.table.setItem(row, 3, QTableWidgetItem(str(staff["date_of_birth"])))
                self.table.setItem(row, 4, QTableWidgetItem(str(staff["gender"])))
                self.table.setItem(row, 5, QTableWidgetItem(str(staff["staff_office"])))
                self.table.setItem(row, 6, QTableWidgetItem(activity.get(staff["is_active"])))
                self.table.setCellWidget(row, 7, actions_combo)
        else:
            self.table.hide()
            self.empty_label.show()

        self._filter_staff()

    def _filter_staff(self):
        """Processes instant searches and active filters on the staff grid layout."""
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

            self.table.setRowHidden(row, not (matches_search and matches_status))
