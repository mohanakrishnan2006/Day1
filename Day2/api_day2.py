import json
import requests as request

url="https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 13.08,
    "longitude": 80.27,
    "current": "temperature_2m , wind_speed_10m"
}

try:
    response=request.get(url,params=params,timeout=10)
    print(response.status_code)
    response.raise_for_status() 
    if response.status_code!=200:
        print(f"somethig went wrong: {response.status_code}")
    
    data=response.json()

    temperature=data["current"]["temperature_2m"]
    wind=data["current"]["wind_speed_10m"]
    latitude=data["latitude"]
    longitude=data["longitude"]

    print(f"temperature:{temperature}°C")
    print(f"wind speed:{wind} km/h")
    print(f"latitude:{latitude}")
    print(f"longitude:{longitude}")

except request.exceptions.RequestException as e:
    print(f"request failed: {e}")

