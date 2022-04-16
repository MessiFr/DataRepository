import pandas as pd
import json
import datetime
from sys import argv

with open('../raw_data/twitter-melb-after.json', 'r') as f:
    row_data = json.load(f)

df = pd.DataFrame(columns = {'time', 'lat', 'long', 'friends_count', 'language'})
df = df[['time', 'friends_count', 'lat', 'long', 'language']]

length = int(argv[1])
print(length)

month = {
  "Jan": 1,
  "Feb": 2,
  "Mar": 3,
  "Apr": 4,
  "May": 5,
  "Jun": 6,
  "Jul": 7,
  "Aug": 8,
  "Sep": 9,
  "Oct": 10,
  "Nov": 11,
  "Dec": 12
}

index = 0
for row in row_data['rows']:
    if index >= length:
        break

    if row['doc']['coordinates'] and \
        row['doc']['coordinates']['type']=='Point' and row['doc']['user']['friends_count'] and \
            row['doc']['created_at'] and row['doc']['metadata']['iso_language_code']:

        time_list = row['doc']['created_at'].split()
        
        time_ = datetime.datetime(int(time_list[-1]), month[time_list[1]], int(time_list[2]), int(time_list[3].split(":")[0]), int(time_list[3].split(":")[1]), int(time_list[3].split(":")[2]))    

        df.loc[index, 'time'] = time_
        df.loc[index, 'friends_count'] = row['doc']['user']['friends_count']
        df.loc[index, 'lat'] = row['doc']['coordinates']['coordinates'][1]
        df.loc[index, 'long'] = row['doc']['coordinates']['coordinates'][0]
        df.loc[index, 'language'] = row['doc']['metadata']['iso_language_code']
        index += 1

df.to_csv(f'../csv/twitter-melb-{length}.csv')