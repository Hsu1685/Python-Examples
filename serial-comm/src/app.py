# -*- coding: utf-8 -*-

"""This module provides the RP Renamer application."""

import sys

from PyQt5.QtWidgets import QApplication

from .views import MainWindow


def main():
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the main window
    main_window = MainWindow()
    main_window.show()
    # Run the event loop
    sys.exit(app.exec())
