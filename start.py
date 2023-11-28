# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_start(object):
    def setupUi(self, label1):
        label1.setObjectName("label1")
        label1.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(28)
        label1.setFont(font)
        label1.setStyleSheet("background-color: rgb(219, 207, 255);")
        self.centralwidget = QtWidgets.QWidget(label1)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 531, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(82, 195, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(82, 195, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.lineEdit.setPalette(palette)
        self.lineEdit.setStyleSheet("background-color: rgb(247, 201, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.log_in = QtWidgets.QPushButton(self.centralwidget)
        self.log_in.setGeometry(QtCore.QRect(300, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.log_in.setFont(font)
        self.log_in.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(202, 8, 255);\n"
"background-color: rgb(255, 253, 174);")
        self.log_in.setObjectName("log_in")
        self.registration = QtWidgets.QPushButton(self.centralwidget)
        self.registration.setGeometry(QtCore.QRect(300, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.registration.setFont(font)
        self.registration.setStyleSheet("color: rgb(202, 8, 255);\n"
"background-color: rgb(255, 253, 174);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.registration.setObjectName("registration")
        label1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(label1)
        self.statusbar.setObjectName("statusbar")
        label1.setStatusBar(self.statusbar)

        self.retranslateUi(label1)
        QtCore.QMetaObject.connectSlotsByName(label1)

    def retranslateUi(self, label1):
        _translate = QtCore.QCoreApplication.translate
        label1.setWindowTitle(_translate("label1", "MainWindow"))
        self.lineEdit.setText(_translate("label1", "Окно входа/регистрации пользователя"))
        self.log_in.setText(_translate("label1", "Вход"))
        self.registration.setText(_translate("label1", "Регистрация"))
