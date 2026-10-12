import json
# student=[
#     {"name": "mohan","age": 20,"city": "chennai","score": 90},
#     {"name": "hari","age": 23,"city": "Banglore","score": 80},

# ]

# with open('details.json','w') as f:
#     json.dump(student,f,indent=2)

# with open('details.json','r') as f:
#     Student=json.load(f)
#     for s in Student:
#         print(f"name is {s['name']} and score is {s['score']}")
# data = {
#     "city": "Chennai",
#     "weather": {"temp": 32, "humidity": 70},
#     "forecast": [
#         {"day": "Mon", "temp": 31},
#         {"day": "Tue", "temp": 33},
#     ],
# }

# with open('details.json','w') as f:
#     json.dump(data,f,indent=2)


# print(data["city"])

# print(data["weather"])
# print(data["weather"]["temp"])

# print(data["forecast"])
# print(data["forecast"][0])
# print(data["forecast"][1]["day"])

# for key,value in data.items():
#     print(f"{key} : {value}")   


import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

tasks = load_tasks()
tasks.append({"title": "learn json", "done": False})
save_tasks(tasks)
print(tasks)