# -*- coding: utf-8 -*-
__author__ = 'HHH'

# Import packages
import sys
from PyQt5.Qt import *
from settings import Settings

# Create app
app = QApplication(sys.argv)

# Create setting
settings = Settings()

# Create main window
main_window = QWidget()
main_window.setWindowTitle(settings.window_title)
main_window.show()

# Main project
sys.exit(app.exec())
