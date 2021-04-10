import sys
from PyQt5.Qt import *
from app import app
from settings import Settings

settings = Settings()

class MainWindow(QWidget):
    """Main Window"""

    def __init__(self, width=500, height=500):
        """Initialize as the top window"""
        super().__init__()
        self.resize(width, height)
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface of the main screen"""
        saying = QLabel(self)
        saying.move(100, 100)
        saying.setText('Learning always makes you happy.')


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
