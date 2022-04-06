from requests import get
from time import strftime, gmtime
from tkinter import *

COLOR1 = "#8A8AFF"
COLOR2 = "#BDBDFF"
COLOR3 = "#F0F0FF"

mainWindow = Tk()
mainWindow.title("Weather App")
mainWindow.iconbitmap("appIcon.ico")
mainWindow.geometry("320x500")
mainWindow.config(bg = COLOR3)
mainWindow.resizable(False, False)

enterCityLabel = Label(mainWindow, font=('Manrope', 32, 'bold'), text = "Enter City", bg = COLOR3)
enterCityLabel.grid(row=0, column=0, padx=45, pady=50)

cityEntry = Entry(mainWindow, font=('Manrope', 24), bg = COLOR2, width=15, bd=0, justify=CENTER)
cityEntry.grid(row=1, column=0, padx=9)

goButton = Button(mainWindow, font=('Manrope', 24, 'bold'), text = "Go", bg = COLOR1, bd=0, command=lambda: getWeather(cityEntry.get()))
goButton.grid(row=2, column=0, padx=9, pady=15)

def getWeather(city):
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9f8620325348a6920a0fc0dfaf31ffa2"
    
    jsonData = get(api).json()
    
    if jsonData["cod"] == "404":
        print("City not found")
        return 

    mainWindow.withdraw()
    
    weatherWindow = Tk()
    weatherWindow.title("Weather App")
    weatherWindow.iconbitmap("appIcon.ico")
    weatherWindow.geometry("320x500")
    weatherWindow.config(bg = COLOR3)
    weatherWindow.resizable(False, False)
    
    weatherWindow.mainloop()
    
    condition = jsonData['weather'][0]['main']
    icon = jsonData['weather'][0]['icon']
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

mainWindow.mainloop()