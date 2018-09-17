#-*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import xlrd
import json

data_path = "/Users/maciel/Documents/Model/Modeling-Problems/Terrorists/Script/data.xlsx"
# dataframe = pd.read_excel(data_path, sheet_name=None, header=0)
# print(dataframe)
# print(type(dataframe))

data = xlrd.open_workbook(data_path)
table = data.sheets()[0]
# print(table)
print(table.cell(0, 0).value)
print(table.cell(1, 0).value)
num = table.nrows
print(num)

terrorists = {}
location = []
for i in range(1, num):
    dict = {}
    eventid = str(table.cell(i, 0).value)
    dict['eventid'] = eventid[:5].replace(".", "")
    dict['latitude'] = table.cell(i, 13).value
    dict['longitude'] = table.cell(i, 14).value
    location.append(dict)
print(location)
terrorists["Name"] = "distribution"
terrorists["Location"] = location
jsonObj = json.dumps(terrorists)

fileObject = open('jsonFile.json', 'w')
fileObject.write(jsonObj)
fileObject.close()

# eventid = map(str, table.col_values(0))
# print(eventid)
# new_eventid = [key[:5] for key in eventid]
# print(new_eventid)
# lat = table.col_values(13)
# lon = table.col_values(14)
# print(evnetid, lat, lon)

# new = np.vstack((eventid, lat, lon))
# print(new)

