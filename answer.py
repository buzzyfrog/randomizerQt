from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint

from UI.ui_answer import Ui_Answer


class Answer(QMainWindow, Ui_Answer):
    def __init__(self, parent=None):
        super(Answer, self).__init__(parent)
        self.setupUi(self)
        self.CreateAnswer_2.clicked.connect(self.get_answer)

    def get_answer(self):
        result = randint(1, 2)
        if result == 1:
            final_result = 'ДА'
            self.Image_2.setPixmap(QtGui.QPixmap("src/like.png"))
        else:
            final_result = 'НЕТ'
            self.Image_2.setPixmap(QtGui.QPixmap("src/dislike.png"))

        self.Output_2.setText(final_result)
