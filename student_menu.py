# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 247, 201);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.startTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.startTestButton.setGeometry(QtCore.QRect(300, 340, 161, 41))
        self.startTestButton.setStyleSheet("background-color: rgb(255, 253, 174);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.startTestButton.setObjectName("startTestButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 130, 421, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.codeEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.codeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.codeEdit.setObjectName("codeEdit")
        self.horizontalLayout.addWidget(self.codeEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 151, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 253, 174);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Проверочная работа"))
        self.startTestButton.setText(_translate("MainWindow", "Начать проверочную"))
        self.label_3.setText(_translate("MainWindow", "Код проверочной"))
        self.pushButton.setText(_translate("MainWindow", "<--- Вернуться"))