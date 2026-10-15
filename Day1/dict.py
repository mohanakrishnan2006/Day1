Student=[
    {"name": "mohan","age": 20,"city": "chennai","score": 90},
    {"name": "hari","age": 23,"city": "Banglore","score": 80},
    {"name": "moses","age": 26,"city": "poonamalle","score": 70}

]

# for student in Student:
#     print(f"name is {student['name']} in the city of {student['city']} and age is {student['age']}")

for student in Student:
    if student["score"] >= 90:
        print(f"name is {student['name']} and score is {student['score']} is very good")

scores=[student["score"] for student in Student]
for student in Student:
    scores.append(student["score"])
avg=sum(scores)/len(scores)
print(f"average score is {avg}")
    # elif score>=80:
    #     print(f"name is {name} and score is {score} is good")
    # elif score>=70:
    #     print(f"name is {name} and score is {score} is Avg")
    # else:
    #     print(f"name is {name} and score is {score} is poor")
# print(Student)
# print(Student["name"])
# print("name")
# Student["age"]=21
# Student["dept"]="CSE"
# print(Student)

# for Key,Value in Student.items():
#     print(f" {Key} : {Value}")

# Test

