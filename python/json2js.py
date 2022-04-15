import json

with open('mapConfig.json', 'r') as f:
    data = json.load(f)

print(data)