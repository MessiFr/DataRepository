import csv
import json
from sys import argv

fileName = argv[1].split('.')[0]

csvfile = open(f"../csv/{argv[1]}",'r')

jsonfile = open(f'../json/{fileName}.json', 'w')
 
fieldnames = ("", "time", "friends_count", "lat", "long", "language")
 
reader = csv.DictReader( csvfile, fieldnames)

data = {
  "fields": [
    {"name": "index", "format": "", "type": "real"},
    {"name": "time", "format": "MM dd HH:mm yyyy", "type": "timestamp"},
    {"name": "friends_count", "format": "", "type": "real"},
    {"name": "lat", "format": "", "type": "real"},
    {"name": "long", "format": "", "type": "real"},
    {"name": "language", "format":"", "type": "string"}
  ],
  "rows": []
}

count = 0
for row in [row for row in reader][1:]:
    tmp = [count, row['time'], int(row['friends_count']), float(row['lat']), float(row['long']), row['language']]
    
    count += 1
    data['rows'].append(tmp)

json.dump(data, jsonfile)