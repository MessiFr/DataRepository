import csv
import json
from sys import argv
import pandas as pd

fileName = argv[1].split('.')[0]

df = pd.read_csv(f"{argv[1]}")

jsonfile = open(f'{fileName}.json', 'w')
 
fieldnames = ("lat", "lon", "accum_conv_rain")

data = {
  "fields": [
    {"name": "lat", "format": "", "type": "real"},
    {"name": "lon", "format": "", "type": "real"},
    {"name": "accum_conv_rain", "format": "", "type": "real"},
  ],
  "rows": []
}

for i in range(len(df)):
    tmp = [df.loc[i, 'lat'], df.loc[i, 'lon'], df.loc[i, 'accum_conv_rain']]
    # tmp = [float(df['lat']), float(df['lon']), float(df['accum_conv_rain'])]

    data['rows'].append(tmp)

json.dump(data, jsonfile)