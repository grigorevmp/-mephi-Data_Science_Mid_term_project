import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('PointzAggregator-AirlinesData.xml')
root = tree.getroot()

columns = ['uid', 'FirstName', 'LastName', 'CardNumber', 'BonusProgram','Code', 'Date', 'Departure',
           'Arrival', 'Fare']

id_ = 0
data = []
check = 10000
for user in root:
    for elem in user[1]:
        for activity in elem[1]:
            data.append([user.attrib['uid']])
            data[id_].append(user[0].attrib['first'])
            data[id_].append(user[0].attrib['last'])
            data[id_].append(elem.attrib['number'])
            data[id_].append(elem[0].text)
            data[id_].append(activity[0].text)
            data[id_].append(activity[1].text)
            data[id_].append(activity[2].text)
            data[id_].append(activity[3].text)
            data[id_].append(activity[4].text)
            id_ += 1
            if id_ == check:
                print(id_)
                check += 10000

df = pd.DataFrame(data, columns=columns)
df.to_csv(r'PointzAggregator-AirlinesData.csv', index_label='id')
