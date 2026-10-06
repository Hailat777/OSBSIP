import requests

api_key = "4dff22461c9296160b3f7bbd8ba470aa"
city = input("Enter city name: ")

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

url = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(url, params=params)

print(response.status_code)

data = response.json()

city_name = data["name"]
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]

print("\nWeather Information")
print("-------------------")
print("City:", city_name)
print("Temperature:", temperature, "°C")
print("Feels like:", feels_like, "°C")
print("Weather:", weather)
print("Humidity:", humidity, "%")
print("Wind speed:", wind_speed, "m/s")