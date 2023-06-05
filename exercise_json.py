import json

json_file = open("python_mini_projects\my_json.json", "w+")

json_test = {
    "name": "NiubProgrammer",
    "age": 21,
    "language": ["Python", "JavaScript", "C++"],
    "is_cool": True
}

json.dump(json_test, json_file, indent = 4)

json_file.close()

with open("python_mini_projects\my_json.json", "r") as my_other_json:
    for i in my_other_json.readlines():
        print(i)

