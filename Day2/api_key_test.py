import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MY_API_KEY")
student={
        "name":"mohan",
        "age":20,
        "city":"chennai",
    }

if not api_key:
    print("API key missing. Check your .env file.")
else:
#    Header={"Name":f"Mohan"}
#    response=requests.get("https://httpbin.org/headers",headers=Header,timeout=10)
#    print(response.json())


    headers={
        "authorization":f"bearer {api_key}"
    }
    response=requests.post("https://httpbin.org/anything",json=student,headers=headers,timeout=10)
    response.raise_for_status()
    # print(response.json()["json"])
    result=response.json()
    print("authorization :",result["headers"].get("authorization"))
    auth = next(
        (value for key, value in result["headers"].items()
         if key.lower() == "authorization"),
        None
    )

    print("Authorization:", auth)


