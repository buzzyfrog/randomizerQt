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
        self.textEdit = QtWidgets.QTextEdit(History_form)
        self.textEdit.setGeometry(QtCore.QRect(150, 90, 461, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(History_form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 550, 461, 71))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(History_form)
        QtCore.QMetaObject.connectSlotsByName(History_form)

    def retranslateUi(self, History_form):
        _translate = QtCore.QCoreApplication.translate
        History_form.setWindowTitle(_translate("History_form", "история"))
        self.pushButton.setText(_translate("History_form", "//назад"))
        self.textEdit.setHtml(_translate("History_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("History_form", "очистить сводку действий"))


