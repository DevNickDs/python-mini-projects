import json

json_file = open("python_mini_projects\my_json.json", "w+")

json_test = {
    "name": "NiubProgrammer",
    "age": 21,
    "language": "Python",
    "is_cool": True
}

json.dump(json_test, json_file)