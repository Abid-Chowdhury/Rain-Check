from requests import get
from time import strftime, gmtime

def getWeather(city):
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9f8620325348a6920a0fc0dfaf31ffa2"
    
    jsonData = get(api).json()
    
    if jsonData["cod"] == "404":
        print("City not found")
        return 

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
    
getWeather('London')