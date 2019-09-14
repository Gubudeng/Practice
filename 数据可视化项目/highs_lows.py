import csv

from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取最高气温

#打开文件
file_name = 'death_valley_2018_full.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #从文件中获取日期,最高气温最低气温


#将最高气温数据保存至一个列表中
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        try:
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            pass
        else:
            highs.append(high)
            lows.append(low)
    print(highs)
#查看列表索引
    for index, column_header in enumerate(header_row):
        print(index, column_header)

#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式
plt.title("Daily high temperatures, 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
