import math
import requests
import json

# Use the OpenWeatherAPI to extract accurate weather and climate data
api_key = "7af3710d5bb0ec426ee0f70deabb7592"

base_url = "http://api.openweathermap.org/data/2.5/weather?"


# Using the API, retrieve weather data for the city inputted by the user
def weather(city):
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)

    # save the weather data for the city in a JSON file to parse and display to the user
    city_weather = response.json()

    if city_weather["cod"] == "404":
        print('City not found')

    else:
        local_weather = city_weather["main"]
        temp = (local_weather["temp"] - 273.15) * (9 / 5) + 32
        temp = str(math.floor(temp)) + "\u00B0F"
        pressure = local_weather["pressure"]
        humidity = str(local_weather["humidity"]) + "%"
        weather_data = city_weather["weather"]
        description = weather_data[0]["description"]

        print("Temperature: " + str(temp) + "\nAtmospheric Pressure: " + str(pressure) + "\nHumidity: " + str(
            humidity) + "\nDescription: " + str(description) + ' in ' + str(city).capitalize() + ' right now')


# input city name from user and call function to return weather data for that city
city_name = input('Enter city name: ')
weather(city_name)
