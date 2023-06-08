import requests

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "93af1d7123fdf9a069485b6bcb6c39f5"

params = {
    "q": "Athens",  # Replace "YourCityName" with the actual city name
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
