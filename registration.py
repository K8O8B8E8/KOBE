# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registration(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 253, 174);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.registration_button = QtWidgets.QPushButton(self.centralwidget)
        self.registration_button.setGeometry(QtCore.QRect(300, 320, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.registration_button.setFont(font)
        self.registration_button.setAutoFillBackground(False)
        self.registration_button.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.registration_button.setObjectName("registration_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 140, 431, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.loginEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.loginEdit.setStyleSheet("background-color: rgb(255, 247, 201);")
        self.loginEdit.setObjectName("loginEdit")
        self.gridLayout.addWidget(self.loginEdit, 0, 1, 1, 1)
        self.password1Edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password1Edit.setStyleSheet("background-color: rgb(255, 247, 201);")
        self.password1Edit.setObjectName("password1Edit")
        self.gridLayout.addWidget(self.password1Edit, 1, 1, 1, 1)
        self.password2Edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password2Edit.setStyleSheet("background-color: rgb(255, 247, 201);")
        self.password2Edit.setObjectName("password2Edit")
        self.gridLayout.addWidget(self.password2Edit, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 161, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 247, 201);\n"
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
        self.registration_button.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.label_4.setText(_translate("MainWindow", "Форма регистрации"))
        self.label.setText(_translate("MainWindow", "Повторите пароль"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_3.setText(_translate("MainWindow", "Логин"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ученик"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Учитель"))
        self.label_5.setText(_translate("MainWindow", "Выберете роль"))
        self.pushButton.setText(_translate("MainWindow", "<---   Вернуться"))
