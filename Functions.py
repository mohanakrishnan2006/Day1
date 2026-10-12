# def details(name,city="chennai"):
#     return f"my name is {name} and i live in {city}"

# print(details("mohan"))
# print(details("hari","banglore"))

from webbrowser import get


def Is_passed(student):
    return student["score"]>=80

Student=[
    {"name": "mohan","age": 20,"city": "chennai","score": 90},
    {"name": "hari","age": 23,"city": "Banglore","score": 70},
    {"name": "moses","age": 26,"city": "poonamalle","score": 80}
]

for s in Student:
    print(s["name"],Is_passed(s))


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("this is not a number,invalid input")


age=get_number("enter age ")
print(f"age is {age}")

def divide_error(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("division by zero is not allowed")
    except TypeError:
        print("invalid input type")
    except Exception as e:
        print(f"error is {e}")

a=int(input("enter a number a: "))
b=int(input("enter a number b: "))
print(f"result is {divide_error(a,b)}")