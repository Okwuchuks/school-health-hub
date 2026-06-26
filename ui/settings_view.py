"""
School Health Hub (SHH)
The administrative settings panel for managing dynamic entities and themes.
Author: Ifende Daniel
"""

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QStackedWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QComboBox,
    QHeaderView,
)


class SettingsView(QWidget):
    # Signal to notify the main window to re-apply a new global stylesheet theme string
    theme_changed = Signal(str)

    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self._init_ui()

    def _init_ui(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(15)

        # 1. Left Side Navigation List
        self.nav_list = QListWidget()
        self.nav_list.setFixedWidth(180)
        self.nav_list.addItems(["Staff Roles", "Staff Offices", "Student Hostels", "Personalization"])
        self.nav_list.currentRowChanged.connect(self._switch_setting_tab)

        # 2. Right Side Stacked View Layout Container
        self.container = QStackedWidget()

        # Build individual configuration panels
        self.roles_panel = self._build_crud_panel(
            "Role Name", self.db_manager.get_all_roles, self.db_manager.add_staff_role
        )
        self.offices_panel = self._build_crud_panel(
            "Office Name", self.db_manager.get_all_offices, self.db_manager.add_staff_office
        )
        self.hostels_panel = self._build_crud_panel(
            "Hostel Name", self.db_manager.get_all_hostels, self.db_manager.add_student_hostel
        )
        self.style_panel = self._build_style_panel()

        # Add sub-panels to the layout stack matching the list index exactly
        self.container.addWidget(self.roles_panel)
        self.container.addWidget(self.offices_panel)
        self.container.addWidget(self.hostels_panel)
        self.container.addWidget(self.style_panel)

        main_layout.addWidget(self.nav_list)
        main_layout.addWidget(self.container)
        self.setLayout(main_layout)

    def _switch_setting_tab(self, index):
        self.container.setCurrentIndex(index)

    def _build_crud_panel(self, label_text, fetch_callback, insert_callback):
        """Helper to cleanly build matching functional rows and tables for our dynamic attributes."""
        panel = QWidget()
        layout = QVBoxLayout()

        # Input Stripe
        input_layout = QHBoxLayout()
        input_field = QLineEdit()
        input_field.setPlaceholderText(f"Add new {label_text.lower()}...")

        add_btn = QPushButton("➕ Add")
        input_layout.addWidget(input_field)
        input_layout.addWidget(add_btn)
        layout.addLayout(input_layout)

        # Inventory Display Table
        table = QTableWidget()
        table.setColumnCount(1)
        table.setHorizontalHeaderLabels([label_text])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(table)

        # Refresh UI state method bound locally
        def refresh_table():
            items = fetch_callback()
            table.setRowCount(len(items))
            for index, item in enumerate(items):
                table.setItem(index, 0, QTableWidgetItem(str(item)))

        # Add Action Handler
        def handle_add():
            text = input_field.text().strip()
            if not text:
                QMessageBox.warning(panel, "Input Error", "Field cannot be left empty.")
                return
            insert_callback(text)
            input_field.clear()
            refresh_table()
            QMessageBox.information(panel, "Success", f"Successfully recorded {text}!")

        add_btn.clicked.connect(handle_add)
        refresh_table()  # Initial load populate string assets

        panel.setLayout(layout)
        return panel

    def _build_style_panel(self):
        """Builds your visual theme selector customization cards."""
        panel = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Application Theme Customization")
        title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)

        layout.addWidget(QLabel("Select Active Color Scheme Portfolio:"))
        theme_selector = QComboBox()
        theme_selector.addItems(["🏥 Clinical Teal (Default)", "🌙 Dark Mode Modern", "☀️ Crisp Clean Light"])
        layout.addWidget(theme_selector)

        apply_btn = QPushButton("Apply Visual Styles")
        apply_btn.clicked.connect(lambda: self._handle_theme_swap(theme_selector.currentText()))
        layout.addWidget(apply_btn)

        layout.addStretch()
        panel.setLayout(layout)
        return panel

    def _handle_theme_swap(self, selected_theme):
        """Converts look choices into cascading styling sheets passed to main windows."""
        qss = ""
        if "Teal" in selected_theme:
            qss = """
                QWidget { background-color: #f7f9fa; color: #2c3e50; font-family: 'Segoe UI'; }
                QPushButton { background-color: #008080; color: white; border-radius: 6px; padding: 6px; font-weight: bold; }
                QPushButton:hover { background-color: #006666; }
                QLineEdit, QComboBox { background-color: white; border: 1px solid #ccd1d9; border-radius: 4px; padding: 4px; }
                QTableWidget { background-color: white; gridline-color: #e6e9ed; }
            """
        elif "Dark" in selected_theme:
            qss = """
                QWidget { background-color: #1e1e2e; color: #cdd6f4; font-family: 'Segoe UI'; }
                QPushButton { background-color: #b4befe; color: #11111b; border-radius: 6px; padding: 6px; font-weight: bold; }
                QPushButton:hover { background-color: #a6e3a1; }
                QLineEdit, QComboBox { background-color: #313244; color: white; border: 1px solid #45475a; border-radius: 4px; padding: 4px; }
                QTableWidget { background-color: #181825; gridline-color: #313244; }
            """
        else:  # Classic Light Mode
            qss = """
                QWidget { background-color: #ffffff; color: #333333; font-family: 'Segoe UI'; }
                QPushButton { background-color: #4a90e2; color: white; border-radius: 6px; padding: 6px; }
                QPushButton:hover { background-color: #357abd; }
                QLineEdit, QComboBox { background-color: #f5f5f5; border: 1px solid #cccccc; padding: 4px; }
            """
        self.theme_changed.emit(qss)
        QMessageBox.information(self, "Theme Applied", "The stylesheet configuration has updated successfully!")
