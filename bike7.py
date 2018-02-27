import csv
from pprint import pprint # 用于输出字典等数据结构

#计算每个月的平均骑行时间
def month_mean_duration(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theMonthDict = {}
        for row in reader:
            if row['month'] in theMonthDict:
                theMonthDict[row['month']] += float(row['duration'])
            else:
                theMonthDict[row['month']] = float(row['duration'])

        return theMonthDict

city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv'}

for city, filename in city_info.items():
    durList = month_mean_duration(filename)
    pprint('{} : {}'.format(city, durList))
