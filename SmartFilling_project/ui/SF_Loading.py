# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SF_Loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SF_Loading(object):
    def setupUi(self, SF_Loading):
        SF_Loading.setObjectName("SF_Loading")
        SF_Loading.resize(1500, 900)
        SF_Loading.setStyleSheet(".QWidget\n"
"{\n"
"    background-color: rgb(255, 255, 255);    \n"
"    border-radius: 70px;\n"
"}\n"
"QFrame#background\n"
"{\n"
"    background-color: rgb(255, 255, 255);    \n"
"    border-radius: 70px;\n"
"}\n"
"QLabel#loading\n"
"{\n"
"    border-image: url(:/loading_icon/loading/big_loading.gif);\n"
"}\n"
"QLabel#logo\n"
"{\n"
"    border-image: url(:/logo/icon/main.png);\n"
"}\n"
"QLabel#loading2\n"
"{\n"
"    border-image: url(:/loading_icon/loading/long_loading.gif);\n"
"}\n"
"QProgressBar#loading_bar\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(207, 207, 207, 255), stop:0.389474 rgba(250, 250, 250, 255), stop:0.505263 rgba(250, 250, 250, 255), stop:0.615789 rgba(250, 250, 250, 255), stop:1 rgba(225, 225, 225, 255));\n"
"    border-style:none;\n"
"    border-radius: 10px;\n"
"    font: 20pt \"Edwardian Script ITC\";\n"
"}\n"
"QProgressBar#loading_bar::chunk\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.494045, x2:1, y2:0.494318, stop:0 rgba(255, 255, 67, 255), stop:0.263158 rgba(112, 255, 147, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.731579 rgba(170, 170, 255, 255), stop:1 rgba(255, 184, 212, 255));\n"
"}\n"
"QLabel#tips\n"
"{\n"
"    font: 24pt \"华文楷体\";\n"
"    text_align:center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SF_Loading)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1404, 810))
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.loading = QtWidgets.QLabel(self.background)
        self.loading.setGeometry(QtCore.QRect(530, 40, 350, 350))
        self.loading.setText("")
        self.loading.setObjectName("loading")
        self.loading_bar = QtWidgets.QProgressBar(self.background)
        self.loading_bar.setGeometry(QtCore.QRect(0, 410, 1401, 21))
        font = QtGui.QFont()
        font.setFamily("Edwardian Script ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loading_bar.setFont(font)
        self.loading_bar.setProperty("value", 0)
        self.loading_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_bar.setOrientation(QtCore.Qt.Horizontal)
        self.loading_bar.setInvertedAppearance(False)
        self.loading_bar.setObjectName("loading_bar")
        self.tips = QtWidgets.QLabel(self.background)
        self.tips.setGeometry(QtCore.QRect(500, 620, 400, 40))
        self.tips.setText("")
        self.tips.setAlignment(QtCore.Qt.AlignCenter)
        self.tips.setObjectName("tips")
        self.logo = QtWidgets.QLabel(self.background)
        self.logo.setGeometry(QtCore.QRect(40, 20, 153, 100))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.loading2 = QtWidgets.QLabel(self.background)
        self.loading2.setGeometry(QtCore.QRect(610, 490, 183, 40))
        self.loading2.setText("")
        self.loading2.setObjectName("loading2")
        SF_Loading.setCentralWidget(self.centralwidget)

        self.retranslateUi(SF_Loading)
        QtCore.QMetaObject.connectSlotsByName(SF_Loading)

    def retranslateUi(self, SF_Loading):
        _translate = QtCore.QCoreApplication.translate
        SF_Loading.setWindowTitle(_translate("SF_Loading", "MainWindow"))
import picture.ui_resource_rc
