

import requests
import json
import geopandas
import geopy
from geopy.geocoders import Nominatim

adress=str(input("What is the address? "))

locator = Nominatim(user_agent='myGeocoder')
location = locator.geocode(adress)

u_lat=str((location.latitude))
u_long=str((location.longitude))

#inital request for forecast data for region
url = 'https://api.weather.gov/points/'
url=url+u_lat+','+u_long
response = requests.get(url)
obj = json.loads(response.text)

# get properties from response - will tell u fds what elements we can use
properties = obj["properties"]
stationlocation_url=properties["forecastOffice"]
station_response_json = requests.get(stationlocation_url)
station_dict = json.loads(station_response_json.text)
station_name = station_dict["name"]
print('')
print('Forecast Provided by: ', station_name)
# get forecast property which is a URL to forecast data
forecast_url = properties["forecastHourly"]

# create new request for forecast data
forecast_response_json = requests.get(forecast_url)
forecast_dict = json.loads(forecast_response_json.text)
forecast_properties = forecast_dict["properties"]


forecast_periods = forecast_properties['periods']
for i in range(25):
    tmp=forecast_periods[i]
    print('Time', tmp['startTime'])
    print('Temperature', tmp['temperature'])
    print('Wind', tmp['windSpeed'])
    print('Description', tmp['shortForecast'])
    print(' ')

daily_forcast_url=properties["forecast"] 


daily_forecast_response_json = requests.get(daily_forcast_url)
daily_forecast_dict = json.loads(daily_forecast_response_json.text)
daily_forecast_properties = daily_forecast_dict["properties"]

daily_forecast_periods = daily_forecast_properties['periods']

for i in range(11):
    forecast=daily_forecast_periods[i]
    print('When?', forecast['name'])
    print(forecast['detailedForecast'])
    print(" ")

