from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.ui_cubes import Ui_Cubes


class Cubes(QMainWindow, Ui_Cubes):
    def __init__(self, parent=None):
        super(Cubes, self).__init__(parent)
        self.setupUi(self)
