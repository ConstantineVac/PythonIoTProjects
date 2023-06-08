import requests

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "your_api_key"

params = {
    "q": "your_city",  # Replace "YourCityName" with the actual city name
    "appid": api_key,
    "units": "metric"  # You can change the units to "imperial" for Fahrenheit
}


response = requests.get(url, params=params)
data = response.json()


if response.status_code == 200:
    temperature = data["main"]["temp"]
    print(f"The current temperature is {temperature}°C")
else:
    print("Error:", data["message"])
