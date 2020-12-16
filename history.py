from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.ui_history import Ui_History_form


class History(QMainWindow, Ui_History_form):
    def __init__(self, parent=None):
        super(History, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.delete_history)
        self.pushButton.clicked.connect(self.close)

    def show_history(self):
        with open('db.txt', 'r+') as file:
            txt = file.read()
        self.textEdit.setText(txt)

    def delete_history(self):
        with open('db.txt', 'w') as file:
            file.truncate()
        with open('db.txt', 'r') as file:
            txt = file.read()
        self.textEdit.setText(txt)
