import json


dict = {"student": {
    "name" : "dang hai",
    "age" : 29,
    "address": "Antony"
}}

with open("./newjson-file.json", "w") as write_json_file:
    json.dump(dict, write_json_file)
