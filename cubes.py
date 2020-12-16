from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from UI.ui_cubes import Ui_Cubes

class Cubes(QMainWindow, Ui_Cubes):
    def __init__(self, parent=None):
        super(Cubes, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_drop.clicked.connect(self.roll_cubes)
        self.pushButton_back.clicked.connect(self.close)

    # function for checking combobox item
    def roll_cubes(self):
        n = int(self.comboBox.currentText())
        res = [randint(1, 6) for _ in range(n)]
        res_final = sum(res)
        # output result
        self.Label_cube_1.setText(str(res))
        self.Output.setText(str(res_final))
        # write result to the file
        with open('db.txt', 'a', encoding='utf-8') as file:
            file.write("Количество кубиков: " + str(n) + ";" + " сумма: " + str(res_final) + ";" + '\n')


