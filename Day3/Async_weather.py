import asyncio
import time
import httpx
cities={
    "chennai":(13.08, 80.27),
    "delhi": (28.61, 77.21),
    "mumbai": (19.08, 72.88),
    "kolkata": (22.57, 88.36),
    "bangalore": (09.99, 77.59),

}

URL = "https://api.open-meteo.com/v1/forecast"
async def get_weather(client, city, lat, lon):
    params = {"latitude": lat, "longitude": lon, "current": "temperature_2m"}
    try:
        response = await client.get(URL, params=params, timeout=20)
        response.raise_for_status()
        return city, response.json()["current"]["temperature_2m"]
    except httpx.HTTPError:
        return city, None
async def main():
    start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        tasks = [get_weather(client, city, lat, lon) for city, (lat, lon) in cities.items()]
        results = await asyncio.gather(*tasks)

    for city, temp in results:
        if temp is None:
            print(f"{city.title()}: failed")
        else:
            print(f"{city.title()}: {temp} °C")
    print(f"async time: {time.perf_counter() - start:.2f} seconds")

asyncio.run(main())