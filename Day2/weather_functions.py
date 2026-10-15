import requests

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["current"]["temperature_2m"]   
     # return the temperature from data
    except requests.exceptions.RequestException:
        return None         # something failed



cities={
    "chennai": (13.08, 80.27),
    "delhi": (28.61, 77.23),
    "mumbai":(19.08, 72.88),
}

city=input("enter a city :").lower().strip()

if city in cities:
    lat,lon=cities[city]
    temperature=get_weather(lat,lon)

    if temperature is not None:
        print(f"temperature in {city.title()} is {temperature} ")
    else:
        print(f"could not get weather")
else:
    print("city not found")