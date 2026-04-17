"""
School Health Hub (SHH)
Entry point for the application.
Author: Ifende Daniel
"""

import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


# -----THE FUNCTION WHICH EXECUTES THE MAIN WINDOW..
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
