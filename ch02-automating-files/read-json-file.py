import json
# pprint module automatically formats Python objects for printing, it output often more easily to read.
from pprint import pprint

with open("./json-file.json", "r") as read_jsonfile:
    content = json.load(read_jsonfile)
    print(type(content))
    print(content)
    pprint(content)
