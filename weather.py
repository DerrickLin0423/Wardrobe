import requests
import json

class Weather:
    def __init__(self, zip=92887):
        self.weatherAPI = ''
        self.zip = zip
        self.currentTemp = 0 # in Fahrenheit
        self.minTemp = 0 # in Fahrenheit
        self.maxTemp = 0 # in Fahrenheit
        
        self._getWeatherAPI()
        self._getWeatherData()

    def _getWeatherAPI(self):
        with open("Resources/weather_api.txt") as f:
            self.weatherAPI = f.readline()
    
    def _getWeatherData(self):
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={self.zip},us&appid={self.weatherAPI}&units=imperial')
        if r.status_code == 401:
            print("bad request")
            return
        jsonObj = json.loads(r.text)
        self.currentTemp = float(jsonObj['main']['temp'])
        self.minTemp = float(jsonObj['main']['temp_min'])
        self.maxTemp = float(jsonObj['main']['temp_max'])

if __name__ == "__main__":
    w = Weather()
    print(w.currentTemp)
    print(w.minTemp)
    print(w.maxTemp)
    
