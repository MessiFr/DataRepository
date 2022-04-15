import pandas as pd
import json
from sys import argv

with open('../raw_data/twitter-melb-after.json', 'r') as f:
    row_data = json.load(f)

df = pd.DataFrame(columns = {'time', 'lat', 'long', 'friends_count', 'language'})
df = df[['time', 'friends_count', 'lat', 'long', 'language']]

length = int(argv[1])
print(length)

month = {
  "Jan": "01",
  "Feb": "02",
  "Mar": "03",
  "Apr": "04",
  "May": "05",
  "Jun": "06",
  "Jul": "07",
  "Aug": "08",
  "Sep": "09",
  "Oct": "10",
  "Nov": "11",
  "Dec": "12"
}

index = 0
for row in row_data['rows']:
    if index >= length:
        break

    if row['doc']['coordinates'] and \
        row['doc']['coordinates']['type']=='Point' and row['doc']['user']['friends_count'] and \
            row['doc']['created_at'] and row['doc']['metadata']['iso_language_code']:
        # month_ = month(row['doc']['created_at'].split()[])
        time_ = row['doc']['created_at'].split()[1:4]
        time_[0] = month[time_[0]]
        year = row['doc']['created_at'].split()[-1]
        time_.append(year)
        df.loc[index, 'time'] = ' '.join(time_)
        df.loc[index, 'friends_count'] = row['doc']['user']['friends_count']
        df.loc[index, 'lat'] = row['doc']['coordinates']['coordinates'][1]
        df.loc[index, 'long'] = row['doc']['coordinates']['coordinates'][0]
        df.loc[index, 'language'] = row['doc']['metadata']['iso_language_code']
        index += 1

df.to_csv(f'../csv/twitter-melb-{length}.csv')