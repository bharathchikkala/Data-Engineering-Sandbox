'''
For weather documention go through this link: https://openweathermap.org/api/current?collection=current_forecast
For API_KEY login to above link and get your unique key
To find your latitud and longitude of your place: https://www.latlong.net/
'''

import requests
weather_parameters = {
    "lat" : 16.572090,
    "lon" : 82.000854,
    "appid" : "985dbb049de5ec1aa9b90edfb1cf7257",
    "cnt" : 10
}
response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast",params=weather_parameters)
response.raise_for_status()
data = response.json()
#print(data)
# print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data['list']:
    weather_id = hour_data['weather'][0]['id']
    print(weather_id)
    if weather_id < 700:
        will_rain = True

if will_rain:
    print("Bring Umbrella")
else:
    print("No rain")
