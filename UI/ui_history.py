# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_History_form(object):
    def setupUi(self, History_form):
        History_form.setObjectName("History_form")
        History_form.resize(771, 770)
        self.pushButton = QtWidgets.QPushButton(History_form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(History_form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 550, 451, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(History_form)
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 451, 481))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.retranslateUi(History_form)
        QtCore.QMetaObject.connectSlotsByName(History_form)

    def retranslateUi(self, History_form):
        _translate = QtCore.QCoreApplication.translate
        History_form.setWindowTitle(_translate("History_form", "история"))
        self.pushButton.setText(_translate("History_form", "//назад"))
        self.pushButton_2.setText(_translate(
            "History_form", "очистить сводку действий"))
