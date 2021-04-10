import os
from os.path import dirname
from os import sep
from PyQt5.Qt import *
from app import app

class Settings:
    def __init__(self):
        self.source_path = dirname(dirname(__file__)) + sep + 'source'
        self.icon_path = self.source_path + sep + 'icon.png'  # str
        self.icon = QIcon(self.icon_path)
        self.window_title = 'Learning Notes'


if __name__ == '__main__':
    settings = Settings()
