import json
import pandas as pd
import json

# FrequentFlyerForum-Profiles.json #TODO

with open('FrequentFlyerForum-Profiles.json', 'r+') as f:
    frequentFlyerForum_file_ = json.load(f)

frequentFlyerForum = pd.read_json('FrequentFlyerForum-Profiles.json')

columns = ['Nickname', 'First Name', 'Last Name', 'Sex', 'Date', 'Flight', 'Codeshare', 'Depart_City',
           'Depart_Airport', 'Depart_Country', 'Arrival_City', 'Arrival_Airport', 'Arrival_Country']
data = []
loyal_prog_columns = ['Nickname', 'Status', 'Programm', 'Number']
loyal_prog = []
index = 0
ind = 0
for profile in frequentFlyerForum_file_["Forum Profiles"]:
    for flight in profile['Registered Flights']:
        data.append([profile['NickName']])
        data[index].append(profile['Real Name']['First Name'])
        data[index].append(profile['Real Name']['Last Name'])
        data[index].append(profile['Sex'])
        data[index].append(flight['Date'])
        data[index].append(flight['Flight'])
        data[index].append(flight['Codeshare'])
        data[index].append(flight['Departure']['City'])
        data[index].append(flight['Departure']['Airport'])
        data[index].append(flight['Departure']['Country'])
        data[index].append(flight['Arrival']['City'])
        data[index].append(flight['Arrival']['Airport'])
        data[index].append(flight['Arrival']['Country'])
        index += 1
    for lp in profile['Loyality Programm']:
        loyal_prog.append([profile['NickName']])
        loyal_prog[ind].append(lp['Status'])
        loyal_prog[ind].append(lp['programm'])
        loyal_prog[ind].append(lp['Number'])
        ind += 1

df = pd.DataFrame(data, columns=columns)
df.to_csv(r'Registered Flights.csv')
df = pd.DataFrame(loyal_prog, columns=loyal_prog_columns)
df.to_csv(r'Loyality Programm.csv')

# 'Forum Profiles'
# 'Registered Flights', 'NickName', 'Travel Documents', 'Sex', 'Loyality Programm', 'Real Name'
# 'Registered Flights':: 'Date', 'Codeshare', 'Arrival', 'Flight', 'Departure'
