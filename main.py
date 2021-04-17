# -*- coding: utf-8 -*-
__author__ = 'HHH'

from __init__ import *


class Main:
    """The main project"""
    
    def __init__(self):
        self.main_window = MainWindow()
        self.log = InfoLog(self.main_window)
        self.saying = QLabel(self.main_window)
        
    def setup_ui(self):
        self.log.log("What a log!")
        
        self.saying.move(100, 100)
        self.saying.resize(300, 100)
        self.saying.setText('Learning always makes you happy.')

    def main(self):
        self.setup_ui()
        self.main_window.show()

    def update(self):
        while True:
            self.log.setup()

if __name__ == '__main__':
    main_proj = Main()
    main_proj.main()
    sys.exit(app.exec())
