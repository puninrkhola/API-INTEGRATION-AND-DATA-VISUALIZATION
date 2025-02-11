import requests
import json

api_key = "de8118032239de63a57e258196db25ab"  # Your API key
city = "Bengaluru"  # Change it to any city you want

# API URL to fetch the weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Sending GET request
response = requests.get(url)

# Checking if request was successful
if response.status_code == 200:
    data = response.json()
    print(f"Weather in {data['name']}, {data['sys']['country']}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels Like: {data['main']['feels_like']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description'].capitalize()}")
else:
    print("Failed to retrieve data, please check the API key or city name.")
