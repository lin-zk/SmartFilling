# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SF_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SF_Login(object):
    def setupUi(self, SF_Login):
        SF_Login.setObjectName("SF_Login")
        SF_Login.resize(530, 380)
        SF_Login.setMinimumSize(QtCore.QSize(530, 380))
        SF_Login.setMaximumSize(QtCore.QSize(530, 380))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(9)
        SF_Login.setFont(font)
        SF_Login.setStyleSheet("QLabel#welcome\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.1 rgba(207, 253, 255, 255), stop:0.368421 rgba(159, 241, 250, 255), stop:0.6 rgba(153, 247, 255, 255), stop:0.810526 rgba(157, 242, 255, 255));\n"
"    color:qlineargradient(spread:pad, x1:0.505263, y1:0, x2:0.5, y2:1, stop:0.110526 rgba(131, 208, 246, 255), stop:0.726316 rgba(192, 165, 254, 255));\n"
"}\n"
"QLabel#error_tip,QLabel#signup_tip\n"
"{\n"
"    font: 9pt \"等线\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
".QWidget\n"
"{\n"
"    background-color:rgb(253, 251, 242)\n"
"}\n"
"QPushButton#sign_up,QPushButton#help\n"
"{\n"
"    \n"
"    background-color: rgb(253, 251, 242);\n"
"    border-radius:0px;\n"
"    font: 9pt \"等线\";\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QPushButton#sign_up:hover,QPushButton#help:hover\n"
"{\n"
"    font: 9pt \"等线\";\n"
"    color: rgb(75, 75, 75);\n"
"}\n"
"QPushButton#sign_up:pressed,QPushButton#help:pressed\n"
"{\n"
"    font: 9pt \"等线\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton#login\n"
"{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.505263, y1:0, x2:0.5, y2:1, stop:0.121053 rgba(184, 255, 236, 255), stop:0.852632 rgba(69, 249, 199, 255));\n"
"    border-radius:13px;\n"
"    font: 14pt \"华文仿宋\" bold;\n"
"    color: rgb(0, 0, 108)\n"
"}\n"
"QPushButton#login:hover\n"
"{\n"
"    background-color:qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.495, y2:0.023, stop:0.121053 rgba(142, 255, 225, 255), stop:0.852632 rgba(22, 249, 186, 255));\n"
"    font: 14pt \"华文仿宋\" bold;\n"
"    color: rgb(99, 0, 74);\n"
"    border:1px solid rgb(0, 170, 255)\n"
"}\n"
"QPushButton#login:pressed\n"
"{\n"
"    background-color:rgb(75, 225, 255);\n"
"    border-radius:13px;\n"
"    font: 14pt \"华文仿宋\" bold;\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(0, 170, 255)\n"
"}\n"
"QLineEdit\n"
"{\n"
"    font: 11pt \"宋体\";\n"
"    background-color: rgb(253, 251, 242);\n"
"    border:none;\n"
"    border-bottom:1px solid rgb(255, 230, 185);\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border-bottom:1px solid rgb(255, 185, 71);\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    background-color: rgb(254, 254, 254);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"")
        self.welcome = QtWidgets.QLabel(SF_Login)
        self.welcome.setGeometry(QtCore.QRect(0, 0, 530, 160))
        self.welcome.setMinimumSize(QtCore.QSize(0, 160))
        self.welcome.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.welcome.setFont(font)
        self.welcome.setAutoFillBackground(False)
        self.welcome.setObjectName("welcome")
        self.main = QtWidgets.QWidget(SF_Login)
        self.main.setGeometry(QtCore.QRect(0, 140, 530, 241))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setItalic(False)
        self.main.setFont(font)
        self.main.setObjectName("main")
        self.sign_up = QtWidgets.QPushButton(self.main)
        self.sign_up.setGeometry(QtCore.QRect(0, 210, 60, 30))
        self.sign_up.setObjectName("sign_up")
        self.help = QtWidgets.QPushButton(self.main)
        self.help.setGeometry(QtCore.QRect(470, 210, 60, 30))
        self.help.setObjectName("help")
        self.login = QtWidgets.QPushButton(self.main)
        self.login.setGeometry(QtCore.QRect(135, 165, 240, 40))
        self.login.setMinimumSize(QtCore.QSize(240, 40))
        self.login.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("华文仿宋 13")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.main)
        self.password.setGeometry(QtCore.QRect(135, 105, 240, 30))
        self.password.setMinimumSize(QtCore.QSize(240, 30))
        self.password.setMaximumSize(QtCore.QSize(240, 30))
        self.password.setText("")
        self.password.setMaxLength(20)
        self.password.setFrame(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.username = QtWidgets.QLineEdit(self.main)
        self.username.setEnabled(True)
        self.username.setGeometry(QtCore.QRect(135, 55, 240, 30))
        self.username.setMinimumSize(QtCore.QSize(240, 30))
        self.username.setMaximumSize(QtCore.QSize(240, 30))
        self.username.setText("")
        self.username.setMaxLength(20)
        self.username.setObjectName("username")
        self.signup_tip = QtWidgets.QLabel(self.main)
        self.signup_tip.setGeometry(QtCore.QRect(0, 180, 120, 40))
        self.signup_tip.setMinimumSize(QtCore.QSize(120, 40))
        self.signup_tip.setMaximumSize(QtCore.QSize(120, 40))
        self.signup_tip.setObjectName("signup_tip")
        self.error_tip = QtWidgets.QLabel(self.main)
        self.error_tip.setGeometry(QtCore.QRect(180, 210, 150, 20))
        self.error_tip.setText("")
        self.error_tip.setAlignment(QtCore.Qt.AlignCenter)
        self.error_tip.setObjectName("error_tip")
        self.main.raise_()
        self.welcome.raise_()

        self.retranslateUi(SF_Login)
        QtCore.QMetaObject.connectSlotsByName(SF_Login)

    def retranslateUi(self, SF_Login):
        _translate = QtCore.QCoreApplication.translate
        SF_Login.setWindowTitle(_translate("SF_Login", "Dialog"))
        self.welcome.setText(_translate("SF_Login", "       Welcome！"))
        self.sign_up.setWhatsThis(_translate("SF_Login", "<html><head/><body><p>点击注册</p></body></html>"))
        self.sign_up.setText(_translate("SF_Login", "注册"))
        self.help.setWhatsThis(_translate("SF_Login", "<html><head/><body><p>打开用户使用指南</p></body></html>"))
        self.help.setText(_translate("SF_Login", "帮助"))
        self.login.setText(_translate("SF_Login", "登   录"))
        self.password.setPlaceholderText(_translate("SF_Login", "密码"))
        self.username.setPlaceholderText(_translate("SF_Login", "账号"))
        self.signup_tip.setText(_translate("SF_Login", "没有账号？\n"
"点击↓进行注册"))
