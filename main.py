import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "bc7a7b3d50e2af706acdca4fcf5e4b35"

lat = input('Give latitude for your specified location.\n')
long = input('Give longitude for your specified location.\n')

weather_params = {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

willRain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        willRain = True

if willRain:
    print('It will rain')
else:
    print('It will not rain')