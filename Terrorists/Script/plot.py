#-*- coding: UTF-8 -*-

# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.dates import AutoDateLocator, DateFormatter
#
# df = pd.read_csv('time.csv',  parse_dates=['time'])
# plt.plot_date(df.time, df.nums, fmt='b.')
#
# ax = plt.gca()
# ax.xaxis.set_major_formatter(DateFormatter('%Y'))  #设置时间显示格式
# ax.xaxis.set_major_locator(AutoDateLocator(maxticks=24))       #设置时间间隔
#
# plt.xticks(rotation=90, ha='center')
# label = ['nums']
# plt.legend(label, loc='upper right')
#
# plt.grid()
#
# ax.set_title(u'每年发生恐怖袭击数量', fontproperties='SimHei',fontsize=14)
# ax.set_xlabel('year')
# ax.set_ylabel('nums')
#
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 读取需要绘图的数据
data = pd.read_csv('time.csv')

dict = {}
for key, value in zip(data.time, data.nums):
    # key = datetime.strptime(str(key), '%Y').date()
    dict[key] = value
newlist = sorted(dict.items(), key=lambda x:x[0])
# print(newlist)
years = []
nums = []
for val in newlist:
    years.append(val[0])
    nums.append(val[1])

xs = [datetime.strptime(str(d), '%Y').date() for d in years]

# article_reading.date = pd.to_datetime(article_reading.time)
# 取出8月份至9月28日的数据
# sub_data = article_reading.loc[article_reading.date >= '2017-08-01' ,:]

# 设置图框的大小
fig = plt.figure(figsize=(12,8))
# 绘图
plt.plot(xs, # x轴数据
         nums, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 3, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 5, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='red') # 点的填充色

# 添加标题和坐标轴标签
plt.title("Terrorists")
plt.xlabel('year')
plt.ylabel('nums')

# 剔除图框上边界和右边界的刻度
plt.tick_params(top = 'off', right = 'off')

# 为了避免x轴日期刻度标签的重叠，设置x轴刻度自动展现，并且45度倾斜
fig.autofmt_xdate(rotation = 45)

# 显示图形
plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# from datetime import datetime

# data = pd.read_csv('time.csv')
#
# dict = {}
# for key, value in zip(data.time, data.nums):
#     # key = datetime.strptime(str(key), '%Y').date()
#     dict[key] = value
# newlist = sorted(dict.items(), key=lambda x:x[0])
# # print(newlist)
# years = []
# nums = []
# for val in newlist:
#     years.append(val[0])
#     nums.append(val[1])
# print(years, nums)
# plt.plot(years, nums, 'o-')
# plt.show()

# xs = [datetime.strptime(str(d), '%Y').date() for d in data.time]
# plt.plot(xs, data.nums, 'o-')
# plt.show()

