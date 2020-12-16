from PyQt5 import QtWidgets
from UI.ui_main import Ui_MainWindow
from UI.ui_answer import Ui_Answer
from PyQt5.QtWidgets import QApplication, QMainWindow
from rules import *
import answer
import letters
import rules
import cubes
import history
import os

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.answer.clicked.connect(self.open_answer)
        self.letters.clicked.connect(self.open_letters)
        self.rules.clicked.connect(self.open_rules)
        self.cubes.clicked.connect(self.open_cubes)
        self.history.clicked.connect(self.open_history)

        # create db.txt file
        if not os.path.isfile("db.txt"):
            with open('db.txt', 'w', encoding='utf-8') as file:
                file.write(' ')
        

    def open_answer(self):
        ans.show()

    def open_letters(self):
        letter.show()

    def open_rules(self):
        rule.show_rules()

    def open_cubes(self):
        cube.show()

    def open_history(self):
        his.show()
        his.show_history()


if __name__ == "__main__":
    import sys

    # create app
    app = QtWidgets.QApplication(sys.argv)
    # main window
    showMain = Main()
    showMain.show()
    # answer
    ans = answer.Answer()
    # letters
    letter = letters.Letters()
    # rules
    rule = rules.Rules()
    # cubes
    cube = cubes.Cubes()
    # history
    his = history.History()
    # run main loop
    sys.exit(app.exec_())
