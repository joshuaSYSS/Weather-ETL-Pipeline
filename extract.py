import requests
import pandas as pd

def extract_weather_data():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
    response = requests.get(url)
    data = response.json()
    temps = data['temperature']['data']
    return temps