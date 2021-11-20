import os

import openpyxl
import pandas as pd

directory = 'YourBoardingPassDotAero'

id_ = 0
data = []
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        xlsx_file = f'{directory}/{filename}'
        xlsx_file_obj = openpyxl.load_workbook(xlsx_file)
        for sheet in xlsx_file_obj.worksheets:
            sheet = xlsx_file_obj[sheet.title]
            data.append([])
            data[id_].append(sheet["H1"].value)  # Sequence
            data[id_].append(sheet["A3"].value)  # Title
            data[id_].append(sheet["B3"].value)  # Name
            data[id_].append(sheet["A5"].value)  # FlightNumber
            data[id_].append(sheet["F3"].value)  # BoardNumber
            data[id_].append(sheet["B7"].value)  # Gate
            data[id_].append(sheet["D5"].value)  # From
            data[id_].append(sheet["D7"].value)  # FromCode
            data[id_].append(sheet["H5"].value)  # To
            data[id_].append(sheet["H7"].value)  # ToCode
            data[id_].append(sheet["A9"].value)  # Date
            data[id_].append(sheet["C9"].value)  # Time
            data[id_].append(sheet["E9"].value)  # Operated
            data[id_].append(sheet["A11"].value)  # BoardingEnded
            data[id_].append(sheet["H11"].value)  # Seat
            data[id_].append(sheet["B13"].value)  # PNR
            data[id_].append(sheet["E13"].value)  # ETicket
            id_ += 1

columns = ['Sequence', 'Title', 'Name', 'FlightNumber', 'BoardNumber',
           'Gate', 'From', 'FromCode', 'To', 'ToCode', 'Date',
           'Time', 'Operated', 'BoardingEnded', 'Seat', 'PNR', 'ETicket']

df = pd.DataFrame(data, columns=columns)
print(df.head())
df.to_csv(r'YourBoardingPassDotAero.csv', index_label='id')
