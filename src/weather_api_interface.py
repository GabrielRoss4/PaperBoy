'''
Interfaces with weather api and returns formatted response
'''

import config as cfg
import requests, traceback
from traceback import print_exc

class WeatherApiInterface(object):
    def __init__(self, api_key=cfg.WEATHER_API_KEY):
        self.api_key = api_key

    def get_weather(self, query):
        try:
            raw_response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?&appid={self.api_key}&zip={query.zipcode},{query.country}&units={query.units}")
            print("Connected to weather API")
            response = raw_response.json()
            return self.format_weather(response)
        except:
            print("Failed to connect to weather API")
            print_exc()
            return -1

    def format_weather(self, api_response):
        return {
            "weather":api_response["weather"][0]["main"], 
            "temp_high":api_response["main"]["temp_max"],
            "temp_low":api_response["main"]["temp_min"],
            "temp_cur":api_response["main"]["temp"],
            "temp_feels_like":api_response["main"]["feels_like"],
            "timezone":api_response["timezone"]//3600,
            "humidity":api_response["main"]["humidity"],
            "wind":api_response["wind"]
            }