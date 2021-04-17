from __init__ import *

settings = Settings()

class MainWindow(QMainWindow):
    """Main Window"""

    def __init__(self, width=500, height=500):
        """Initialize as the top window"""
        super().__init__()
        self.resize(width, height)
        self.setup()

    def setup(self):
        """Set up self"""
        pass

class InfoLog(QLabel):
    """A log in the bottom of a QWidget that logs the information"""
    
    def __init__(self, parent: QWidget = None, height=20):
        super().__init__()
        self.parent = parent
        self.height = height
        self.setup()
        
    def setup(self):
        if self.parent:
            self.setParent(self.parent)
            self.resize(self.parent.width(), self.height)
            self.move(3, self.parent.height() - self.height)
        else:
            self.resize(1000, 50)
            
    def log(self, log_msg=None):
        self.setText(log_msg)
        
    
        
        
        

if __name__ == '__main__':
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
