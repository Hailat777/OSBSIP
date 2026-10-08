import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image,ImageTk
from io import BytesIO
from datetime import datetime

api_key = "1611a768c7c3ffcca0626489c37e48f8"

window =tk.Tk()
window.title("Weather App")
window.geometry("500x750")
title_label=tk.Label(
    window,
    text="Weather App",
    font=("Arial", 24, "bold")

)
title_label.pack(pady=20)

city_entry=tk.Label(
    window,
    text="Enter city name:",
    font=("Arial", 12)

)

city_entry.pack()

city_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=25
)
city_entry.pack(pady=10)

icon_label = tk.Label(window)
icon_label.pack(pady=5)


result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=10)

hourly_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left"
)
hourly_label.pack(pady=10)

daily_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left"
)
daily_label.pack(pady=10)

def get_forecast(city):
    
    forecast_url=(
        "https://api.openweathermap.org/data/2.5/forecast"
    )

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(
            forecast_url,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return None

        return response.json()

    except requests.exceptions.RequestException:

        return None


def get_weather():

    city = city_entry.get().strip()

    if city == "":

        result_label.config(
            text="Please enter a city name."
        )

        hourly_label.config(text="")
        daily_label.config(text="")
        icon_label.config(image="")

        return

   
    weather_url = (
        "https://api.openweathermap.org/data/2.5/weather"
    )

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:

        
        response = requests.get(
            weather_url,
            params=params,
            timeout=10
        )

       
        if response.status_code == 404:

            result_label.config(
                text="City not found. Please enter a valid city."
            )

            hourly_label.config(text="")
            daily_label.config(text="")
            icon_label.config(image="")

            return

       
        if response.status_code != 200:

            result_label.config(
                text="Unable to retrieve weather data."
            )

            hourly_label.config(text="")
            daily_label.config(text="")
            icon_label.config(image="")

            return

       
        data = response.json()


        city_name = data["name"]

        temperature = data["main"]["temp"]

        feels_like = data["main"]["feels_like"]

        humidity = data["main"]["humidity"]

        weather = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        result_label.config(
            text=(
                f"City: {city_name}\n"
                f"Temperature: {temperature} °C\n"
                f"Feels Like: {feels_like} °C\n"
                f"Weather: {weather.title()}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
        )

        icon_code = data["weather"][0]["icon"]

        icon_url = (
            "https://openweathermap.org/img/wn/"
            f"{icon_code}@2x.png"
        )

        icon_response = requests.get(
            icon_url,
            timeout=10
        )

        image_data = Image.open(
            BytesIO(icon_response.content)
        )

        weather_icon = ImageTk.PhotoImage(image_data)

        icon_label.config(
            image=weather_icon
        )

        icon_label.image = weather_icon

        forcast_data = get_forecast(city)

        if forcast_data is None:

            hourly_label.config(
                text="Forecast could not be retrieved."
            )

            daily_label.config(text="")

            return

        forecast_list = forcast_data["list"]

        hourly_text = "NEXT 6 HOURS\n"
        hourly_text += "------------------------------\n"


        for item in forecast_list[:2]:

            date_time = datetime.fromtimestamp(
                item["dt"]
            )

            time = date_time.strftime("%H:%M")

            temp = item["main"]["temp"]

            condition = item["weather"][0]["description"]


            hourly_text += (
                f"{time}   "
                f"{temp:.1f} °C   "
                f"{condition.title()}\n"
            )


        hourly_label.config(
            text=hourly_text
        )
       
        daily_text = "NEXT 5 DAYS\n"
        daily_text += "------------------------------\n"



        daily_forecast = {}


        for item in forecast_list:

            date_time = datetime.fromtimestamp(
                item["dt"]
            )

            date = date_time.date()


            if date not in daily_forecast:

                daily_forecast[date] = item



        count = 0

        for date, item in daily_forecast.items():

            if count >= 5:
                break

            day = date.strftime("%a")

            temp = item["main"]["temp"]

            condition = item["weather"][0]["description"]


            daily_text += (
                f"{day}   "
                f"{temp:.1f} °C   "
                f"{condition.title()}\n"
            )

            count += 1


        daily_label.config(
            text=daily_text
        )


    except requests.exceptions.Timeout:

        result_label.config(
            text="Request timed out. Please try again."
        )

        hourly_label.config(text="")
        daily_label.config(text="")
        icon_label.config(image="")


    except requests.exceptions.ConnectionError:

        result_label.config(
            text="No internet connection."
        )

        hourly_label.config(text="")
        daily_label.config(text="")
        icon_label.config(image="")


    except requests.exceptions.RequestException:

        result_label.config(
            text="Unable to connect to the weather service."
        )

        hourly_label.config(text="")
        daily_label.config(text="")
        icon_label.config(image="")


    except Exception:

        result_label.config(
            text="An unexpected error occurred."
        )

        hourly_label.config(text="")
        daily_label.config(text="")
        icon_label.config(image="")


weather_button = tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather
)

weather_button.pack(pady=10)


window.mainloop()
