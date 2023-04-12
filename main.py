import requests
import json

#Prompt the user for a location
location = input("Please enter your current or preferred location : ")
#enter your API key here in order to access the url as it has been left empty
API_KEY = ' '

#API request URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    #print(data)
    #access the key: value from the json data we have retrieved for each variable
    temperature = data['main']['temp']
    #convert the temp from kelvin to celsius
    temperature_celsius = temperature - 273.15
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    print(f'The temperature in {location} is currently {temperature_celsius:.2f} celsius and humidity is {humidity} with {weather_description}')
else:
    if response.status_code == 404:
        print("Error: Location not found.")
    else:
        print("Error: API request failed.")