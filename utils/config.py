import json

config = {}
# Read data from a JSON file
with open("storage/config.json", encoding="utf-8") as data:
    config = json.load(data)