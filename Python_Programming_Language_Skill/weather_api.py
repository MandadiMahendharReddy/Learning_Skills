# 🌦️ Weather App using OpenWeatherMap API

import requests

# Replace this with your real API key from OpenWeather
API_KEY = "da6197f4f9fa4d482d296c989d10551b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Prepare the request URL with city and API key
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    print(url)

    try:
        # Send the request to the API
        response = requests.get(url)
        data = response.json()

        # If city is found and data is good
        if response.status_code == 200:
            weather = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']}°C",
                "Weather": data["weather"][0]["description"].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']} m/s"
            }

            # Print nicely
            print("Weather Report")
            for key, value in weather.items():
                print(f"{key}: {value}")
        else:
            print("City not found! Please check the name.")

    except Exception as e:
        print("Error occurred:", e)

# Ask user for city name
city = input("Enter a city name: ")
get_weather(city)