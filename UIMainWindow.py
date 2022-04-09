# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowySbPQX.ui'
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


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(320, 500)
        self.centralwidget = QWidget(mainWindow)
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
        self.labelEnterCity = QLabel(self.frame)
        self.labelEnterCity.setObjectName(u"labelEnterCity")
        self.labelEnterCity.setGeometry(QRect(0, 50, 320, 60))
        font = QFont()
        font.setFamily(u"Manrope")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.labelEnterCity.setFont(font)
        self.labelEnterCity.setAlignment(Qt.AlignCenter)
        self.entryCity = QLineEdit(self.frame)
        self.entryCity.setObjectName(u"entryCity")
        self.entryCity.setGeometry(QRect(10, 160, 300, 60))
        font1 = QFont()
        font1.setFamily(u"Manrope")
        font1.setPointSize(24)
        self.entryCity.setFont(font1)
        self.entryCity.setStyleSheet(u"QLineEdit {\n"
"	background-color: #BDBDFF;\n"
"	border-radius: 15px;\n"
"}")
        self.entryCity.setAlignment(Qt.AlignCenter)
        self.buttonGo = QPushButton(self.frame)
        self.buttonGo.setObjectName(u"buttonGo")
        self.buttonGo.setGeometry(QRect(80, 240, 150, 60))
        font2 = QFont()
        font2.setFamily(u"Manrope")
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setWeight(75)
        self.buttonGo.setFont(font2)
        self.buttonGo.setStyleSheet(u"QPushButton {\n"
"	background-color: #8A8AFF;\n"
"	border-radius: 15px;\n"
"}")
        mainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.buttonClose.setText("")
        self.buttonMinimize.setText("")
        self.buttonMaximize.setText("")
        self.labelEnterCity.setText(QCoreApplication.translate("mainWindow", u"Enter City", None))
        self.buttonGo.setText(QCoreApplication.translate("mainWindow", u"Go", None))
    # retranslateUi

