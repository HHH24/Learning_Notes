# -*- coding: utf-8 -*-
__author__ = 'HHH'

# Import packages
import sys
from PyQt5.Qt import *
from app import app
from settings import Settings
from classes import *

main_window = MainWindow()
main_window.show()

# Main project
sys.exit(app.exec())
