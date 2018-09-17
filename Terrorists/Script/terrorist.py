#-*- coding: UTF-8 -*-
from collections import Counter
import xlrd
import json
import csv

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
dates = []
for i in range(1, num):
    dict = {}
    eventid = str(table.cell(i, 0).value)[:5].replace(".", "")
    dates.append(eventid)
    dict['eventid'] = eventid
    dict['latitude'] = table.cell(i, 13).value
    dict['longitude'] = table.cell(i, 14).value
    location.append(dict)
# print(location)

# 转换生成时间跨度文件(time.csv)
time_dict = Counter(dates)
print(time_dict)
with open('time.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['time', 'nums'])
    for key, value in time_dict.items():
       writer.writerow([key, value])

# 转换生成json文件
# terrorists["Name"] = "distribution"
# terrorists["Location"] = location
# jsonObj = json.dumps(terrorists)
#
# fileObject = open('distribution.json', 'w')
# fileObject.write(jsonObj)
# fileObject.close()