from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from UI.ui_letters import Ui_Letters_form


class Letters(QMainWindow, Ui_Letters_form):
    def __init__(self, parent=None):
        super(Letters, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_get.clicked.connect(self.rnd_letter)
        self.pushButton_back.clicked.connect(self.close)
        self.final_result = []

    def rnd_letter(self):
        chars = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        val = randint(1, len(chars))
        result = chars[val].upper()
        self.final_result.append(result)
        self.Output.setText(chars[val])

    def write_fl(self):
        with open('db.txt', 'a') as file:
            file.write("Сгенерированные буквы: ")
            for i in range(len(self.final_result)):
                file.write(self.final_result[i] + ' ')
            file.write('\n')

    def closeEvent(self, event):
        self.write_fl()
