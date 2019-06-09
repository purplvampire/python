#! python3
# quickWeather.py - Prints the weather for a location from the command line.
# APPID must sign up and append to the end of url by &APPID=
import json, requests, sys

# Compute location from command line argument.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
# url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=fde6f4a44afc21c239dba2950f84edcc' % (location)
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData['weather']
print('Current weather in %s:' % (location))
print('Status:', w[0]['main'], '-', w[0]['description'])
