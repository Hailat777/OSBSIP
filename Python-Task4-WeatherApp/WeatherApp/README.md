# Weather App -- Python Programming Internship

**Project:** Task 4 -- Basic Weather Application

## 1. Project Overview

A Python Weather Application developed with Tkinter and the
OpenWeatherMap API. Users enter a city name and retrieve current weather
information through a graphical interface.

## 2. Current Features

-   Tkinter graphical user interface.
-   City input field and Get Weather button.
-   Empty city-input validation.
-   OpenWeatherMap current-weather API integration.
-   Display of city, temperature, feels-like temperature, weather
    condition, humidity, and wind speed.
-   Weather-condition icon retrieved from OpenWeatherMap.
-   Handling of city-not-found and other unsuccessful API responses.
-   Handling of request timeout and connection errors.
-   Current temperature displayed in Celsius (°C).

## 3. Technologies Used

-   Python
-   Tkinter
-   Requests
-   Pillow (PIL)
-   OpenWeatherMap API
-   VS Code
-   Git and GitHub

## 4. How the Application Works

The `get_weather()` function reads the city entered by the user, sends a
request to OpenWeatherMap, checks the response status, extracts the
weather information, and updates the Tkinter interface. The application
also retrieves and displays the appropriate weather icon.

## 5. Error Handling

The application checks for empty input, invalid or unavailable cities,
unsuccessful API responses, request timeouts, connection errors, and
other request exceptions so that common problems are handled gracefully.

## 6. Project Structure

``` text
WeatherApp/
├── WeatherApp.py
└── README.md
```

## 7. Installation and Running

1.  Install Python.
2.  Install the required packages:

``` bash
python -m pip install requests pillow
```

3.  Open `WeatherApp.py` in VS Code.
4.  Configure a valid OpenWeatherMap API key securely.
5.  Run `WeatherApp.py`.
6.  Enter a city name and click **Get Weather**.

## 8. Security Note

Do not publish the OpenWeatherMap API key in a public GitHub repository.
For the final version, use an environment variable or another secure
configuration method.

## 9. Next Features to Implement

-   Finalize the GUI layout and visible labels.
-   Add the next 6 hours hourly forecast.
-   Add the next 5 days daily forecast.
-   Add Celsius/Fahrenheit unit switching.
-   Keep all API and network error messages inside the GUI.
-   Optionally add automatic location detection using an IP-based
    location service.

## 10. Internship Submission

This Weather App is Task 4 of the Python Programming Internship project
work and is maintained together with the other internship projects in
the GitHub repository.

## 11. Author

**Hailu Taye**

Python Programming Internship -- OASIS INFOBYTE
