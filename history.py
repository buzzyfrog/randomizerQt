from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.ui_history import Ui_History_form


class History(QMainWindow, Ui_History_form):
    def __init__(self, parent=None):
        super(History, self).__init__(parent)
        self.setupUi(self)
