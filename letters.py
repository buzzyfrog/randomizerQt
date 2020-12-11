from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.ui_letters import Ui_Letters_form


class Letters(QMainWindow, Ui_Letters_form):
    def __init__(self, parent=None):
        super(Letters, self).__init__(parent)
        self.setupUi(self)
