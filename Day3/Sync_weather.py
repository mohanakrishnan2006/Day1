import time
import requests

cities = {
    "chennai": (13.08, 80.27),
    "delhi": (28.61, 77.21),
    "mumbai": (19.08, 72.88),
    "kolkata": (22.57, 88.36),
    "bangalore": (12.97, 77.59),
}

URL = "https://api.open-meteo.com/v1/forecast"

def get_weather(city, lat, lon):
    params = {"latitude": lat, "longitude": lon, "current": "temperature_2m"}
    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        return city, response.json()["current"]["temperature_2m"]
    except requests.exceptions.RequestException:
        return city, None

start = time.perf_counter()

for city, (lat, lon) in cities.items():
    name, temp = get_weather(city, lat, lon)
    if temp is None:
        print(f"{name.title()}: failed")
    else:
        print(f"{name.title()}: {temp} °C")

print(f"sync time: {time.perf_counter() - start:.2f} seconds")