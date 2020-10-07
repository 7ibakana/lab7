# example URL
# http://api.openweathermap.org/data/2.5/forecast?q=minneapolis&units=imperial&appid=067b8529aa77bd3e479a80ed32f78794
import os
import requests
from pprint import pprint
from datetime import datetime
key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}
url = 'http://api.openweathermap.org/data/2.5/forecast'
data = requests.get(url, params=query).json()
pprint(data)
list_of_forecast = data['list']
if error:
    print('Sorry, could not get weather info')
else:
    for forecast in list_of_forecast:
        temp = forecast['main']['temp']
        wind = forecast['wind']['speed']
        timestamp = forecast['dt']
        forecast_date = datetime.fronttimestamp(timestamp)
        print(f'At {forecast_date} the temperature will be {temp}F and the speed of wind is {wind}')
            