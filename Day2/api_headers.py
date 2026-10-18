import requests

headers = {"X-My-Header": "hello mohan"}

response = requests.get("https://httpbin.org/headers", headers=headers, timeout=10)
print(response.json())

payload={
    "name":"mohan","age":18,"city":"chennai","skills":["python","java"]
}
response=requests.post("https://httpbin.org/post",json=payload,timeout=10)

response.raise_for_status()
print(response.json()["json"])

