# SkyTeam-Exchange.yaml
import yaml
import pandas as pd

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

config_file = "SkyTeam-Exchange.yaml"

stream = open(config_file, "r")
parsed_yaml_file = yaml.load(stream, Loader=Loader)

# a_yaml_file = open("SkyTeam-Exchange.yaml")
# parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
print("Load finished")

id_ = 0
data = []
for date, date_data in parsed_yaml_file.items():
    for flight_num, flight_data in date_data.items():
        for board_num, board_data in flight_data['FF'].items():
            data.append([])
            data[id_].append(date)
            data[id_].append(flight_num)
            data[id_].append(board_num)
            data[id_].append(board_data['CLASS'])
            data[id_].append(board_data['FARE'])
            data[id_].append(flight_data['FROM'])
            data[id_].append(flight_data['STATUS'])
            data[id_].append(flight_data['TO'])
            id_ += 1

columns = ['data', 'FlightNum', 'BoardNum', 'Class', 'Fare', 'From', 'Status', 'To']

df = pd.DataFrame(data, columns=columns)
print(df.head())
df.to_csv(r'SkyTeam-Exchange.csv', index_label='id')
