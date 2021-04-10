import os
from os.path import dirname
from os import sep
from PyQt5.Qt import *

source_path = dirname(dirname(__file__)) + sep + 'source'

icon_path = source_path + sep + 'icon.png'    # str
icon = QIcon(icon_path)
