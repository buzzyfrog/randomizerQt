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
        chars = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        val = randint(0, len(chars) - 1)
        result = chars[val]
        self.final_result.append(result)
        self.Output.setText(chars[val])

    def write_fl(self):
        with open('db.txt', 'a', encoding='utf-8') as file:
            if not self.final_result:
                pass
            else:
                file.write("Сгенерированные буквы: ")
                for i in range(len(self.final_result)):
                    file.write(self.final_result[i] + ' ')
                file.write('\n')

    def closeEvent(self, event):
        self.write_fl()
