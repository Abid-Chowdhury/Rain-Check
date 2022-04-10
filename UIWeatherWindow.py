# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherWindowVZRqSD.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_weatherWindow(object):
    def setupUi(self, weatherWindow):
        if weatherWindow.objectName():
            weatherWindow.setObjectName(u"weatherWindow")
        weatherWindow.resize(320, 500)
        self.centralwidget = QWidget(weatherWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 320, 500))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border-radius: 15px;\n"
"	background-color: #F0F0FF\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.buttonClose = QPushButton(self.frame)
        self.buttonClose.setObjectName(u"buttonClose")
        self.buttonClose.setGeometry(QRect(294, 10, 16, 16))
        self.buttonClose.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,0,0);\n"
"	border-radius: 8px;\n"
"}")
        self.buttonMinimize = QPushButton(self.frame)
        self.buttonMinimize.setObjectName(u"buttonMinimize")
        self.buttonMinimize.setGeometry(QRect(270, 10, 16, 16))
        self.buttonMinimize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 8px;\n"
"}")
        self.buttonMaximize = QPushButton(self.frame)
        self.buttonMaximize.setObjectName(u"buttonMaximize")
        self.buttonMaximize.setGeometry(QRect(244, 10, 16, 16))
        self.buttonMaximize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0,255,0);\n"
"	border-radius: 8px;\n"
"}")
        self.labelTemp = QLabel(self.frame)
        self.labelTemp.setObjectName(u"labelTemp")
        self.labelTemp.setGeometry(QRect(0, 50, 320, 100))
        font = QFont()
        font.setFamily(u"Manrope")
        font.setPointSize(64)
        font.setBold(True)
        font.setWeight(75)
        self.labelTemp.setFont(font)
        self.labelTemp.setStyleSheet(u"QLabel {\n"
"	padding-left: 25px\n"
"}")
        self.labelTemp.setAlignment(Qt.AlignCenter)
        self.labelCondition = QLabel(self.frame)
        self.labelCondition.setObjectName(u"labelCondition")
        self.labelCondition.setGeometry(QRect(0, 150, 320, 60))
        font1 = QFont()
        font1.setFamily(u"Manrope")
        font1.setPointSize(32)
        self.labelCondition.setFont(font1)
        self.labelCondition.setAlignment(Qt.AlignCenter)
        self.labelCity = QLabel(self.frame)
        self.labelCity.setObjectName(u"labelCity")
        self.labelCity.setGeometry(QRect(0, 320, 320, 40))
        font2 = QFont()
        font2.setFamily(u"Manrope SemiBold")
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setWeight(75)
        self.labelCity.setFont(font2)
        self.labelCity.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0)\n"
"}")
        self.labelCity.setAlignment(Qt.AlignCenter)
        self.labelCity_2 = QLabel(self.frame)
        self.labelCity_2.setObjectName(u"labelCity_2")
        self.labelCity_2.setGeometry(QRect(0, 350, 320, 60))
        font3 = QFont()
        font3.setFamily(u"Manrope")
        font3.setPointSize(18)
        self.labelCity_2.setFont(font3)
        self.labelCity_2.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0)\n"
"}")
        self.labelCity_2.setAlignment(Qt.AlignCenter)
        self.buttonClose.raise_()
        self.buttonMinimize.raise_()
        self.buttonMaximize.raise_()
        self.labelTemp.raise_()
        self.labelCondition.raise_()
        self.labelCity_2.raise_()
        self.labelCity.raise_()
        weatherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(weatherWindow)

        QMetaObject.connectSlotsByName(weatherWindow)
    # setupUi

    def retranslateUi(self, weatherWindow):
        weatherWindow.setWindowTitle(QCoreApplication.translate("weatherWindow", u"MainWindow", None))
        self.buttonClose.setText("")
        self.buttonMinimize.setText("")
        self.buttonMaximize.setText("")
        self.labelTemp.setText(QCoreApplication.translate("weatherWindow", u"69\u00b0", None))
        self.labelCondition.setText(QCoreApplication.translate("weatherWindow", u"Cloudy", None))
        self.labelCity.setText(QCoreApplication.translate("weatherWindow", u"London", None))
        self.labelCity_2.setText(QCoreApplication.translate("weatherWindow", u"Saturday | Apr 9 | 10:12", None))
    # retranslateUi

