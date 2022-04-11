import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from requests import get
from time import strftime, gmtime

from weatherApp import *
from UIMainWindow import *
from UIWeatherWindow import *

class UIFunctions(MainWindow):
   
    def openWeatherWindow(self):
        self.UIWeatherWindow = Ui_weatherWindow()
        self.UIWeatherWindow.setupUi(self)
        
        # makes window rounded & removes background
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) 
        
        # move window
        def moveWindow(event):
            if Ui_weatherWindow.returnStatus() == 1:
                Ui_weatherWindow.maximize_restore(self)
            
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
                
        self.UIWeatherWindow.frame.mouseMoveEvent = moveWindow

        # functions
                       
        self.show()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def cityNotFoundError(self, city):
        self.UIMainWindow.labelCityNotFound.setText(f'{city} not found')
        self.UIMainWindow.labelCityNotFound.setHidden(False)   
        
    def getWeather(self, city):
        
        try:
            api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9f8620325348a6920a0fc0dfaf31ffa2"

            jsonData = get(api).json()

            city = jsonData["name"]
            condition = jsonData['weather'][0]['main']
            tempC = int(jsonData['main']['temp'] - 273.15)
            tempF = int(tempC * 9/5 + 32)
            feelsLikeC = int(jsonData['main']['feels_like'] - 273.15)
            feelsLikeF = int(feelsLikeC * 9/5 + 32)
            tempMinC = int(jsonData['main']['temp_min'] - 273.15)
            tempMinF = int(tempMinC * 9/5 + 32)
            tempMaxC = int(jsonData['main']['temp_max'] - 273.15)
            tempMaxF = int(tempMaxC * 9/5 + 32)
            sunrise = strftime('%I:%M:%S %p', gmtime(jsonData['sys']['sunrise'] - 21600))
            sunset = strftime('%I:%M:%S %p', gmtime(jsonData['sys']['sunset'] - 21600))

            self.hide()
            UIFunctions.openWeatherWindow(self)
            
        except KeyError:
            UIFunctions.cityNotFoundError(self, city)
        