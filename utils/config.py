import json

config = {}
# Read data from a JSON file
with open("storage/config.json") as data:
    config = json.load(data)