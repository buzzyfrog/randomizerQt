from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.ui_answer import Ui_Answer


class Answer(QMainWindow, Ui_Answer):
    def __init__(self, parent=None):
        super(Answer, self).__init__(parent)
        self.setupUi(self)
