from requests import get
from time import strftime, gmtime, sleep
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
    
    mainWindow.withdraw()

    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9f8620325348a6920a0fc0dfaf31ffa2"
    jsonData = get(api).json()
    
    if jsonData["cod"] == "404":
        cityNotFoundLabel = Label(mainWindow, font=('Manrope', 24, 'bold'), text = "City Not Found", bg = COLOR3, fg="red")
        cityNotFoundLabel.grid(row=3, column=0, padx=45, pady=50)
        return 

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

    weatherWindow = Tk()
    weatherWindow.title("Weather App")
    weatherWindow.iconbitmap("appIcon.ico")
    weatherWindow.geometry("320x500")
    weatherWindow.config(bg = COLOR3)
    weatherWindow.resizable(False, False)
    
    tempLabel = Label(weatherWindow, font=('Manrope', 64, 'bold'), text = f'{tempF}°', bg = COLOR3)
    tempLabel.grid(row=0, column=0, padx=95)
    
    conditionLabel = Label(weatherWindow, font=('Manrope', 32, 'bold'), text = condition, bg = COLOR3)
    conditionLabel.grid(row=1, column=0, padx=80)
    
    cityLabel = Label(weatherWindow, font=('Manrope', 32, 'bold'), text = city, bg = COLOR3)
    cityLabel.grid(row=2, column=0, padx=25)
    
    weatherWindow.mainloop()

mainWindow.mainloop()