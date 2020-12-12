from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint

from UI.ui_answer import Ui_Answer


class Answer(QMainWindow, Ui_Answer):

    def __init__(self, parent=None):
        super(Answer, self).__init__(parent)
        self.setupUi(self)
        self.CreateAnswer_2.clicked.connect(self.get_answer)
        self.BackBtn.clicked.connect(self.close)
        self.final_result = []

    def get_answer(self):
        result = randint(1, 2)
        if result == 1:
            self.final_result.append('Да')
            self.Image_2.setPixmap(QtGui.QPixmap("src/like.png"))
        else:
            self.final_result.append('Нет')
            self.Image_2.setPixmap(QtGui.QPixmap("src/dislike.png"))
        self.Output_2.setText(self.final_result[-1])

    def write_fl(self):
        with open('db.txt', 'a') as file:
            file.write("Сгенерированные ответы: ")
            for i in range(len(self.final_result)):
                file.write(self.final_result[i] + ' ')
            file.write('\n')

    def closeEvent(self, event):
        self.write_fl()
