import requests

for code in (404, 500):
    try:
        response = requests.get(f"https://httpbin.org/status/{code}", timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{code}: {e}")