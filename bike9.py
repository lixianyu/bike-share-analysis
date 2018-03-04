import csv
from pprint import pprint # 用于输出字典等数据结构
'''
周末和工作日的系统用户骑行模式有何区别？
哪一天会员更可能使用骑行系统？散客呢？
平均骑行时长会受一周内不同日期的影响吗？
'''

def weekly_counts(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theWeekDict = {
        'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
        'Friday':0, 'Saturday':0, 'Sunday':0
        }
        for row in reader:
            theWeekDict[row['day_of_week']] += 1

        return theWeekDict

def weekly_counts_Subscriber(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theWeekDict = {
        'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
        'Friday':0, 'Saturday':0, 'Sunday':0
        }
        for row in reader:
            if row['user_type'] == 'Subscriber':
                theWeekDict[row['day_of_week']] += 1
        return theWeekDict

def weekly_counts_Customer(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theWeekDict = {
        'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
        'Friday':0, 'Saturday':0, 'Sunday':0
        }
        for row in reader:
            if row['user_type'] == 'Customer':
                theWeekDict[row['day_of_week']] += 1
        return theWeekDict

def week_mean_duration(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theWeekDictCounts = {
        'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
        'Friday':0, 'Saturday':0, 'Sunday':0
        }
        theWeekDict = {
        'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
        'Friday':0, 'Saturday':0, 'Sunday':0
        }
        for row in reader:
            dur = float(row['duration'])
            if dur <= 75.0:
                theWeekDict[row['day_of_week']] += dur
                theWeekDictCounts[row['day_of_week']] += 1

        retDict = {}
        for key, val in theWeekDict.items():
            retDict[key] = val / theWeekDictCounts[key]
        return retDict


city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv'}

for city, filename in city_info.items():
    weekDict = weekly_counts(filename)
    pprint('{} : {}'.format(city, weekDict))
    maxKey = max(weekDict, key = weekDict.get)
    print('{}骑行量最大'.format(maxKey))

    weekDictSub = weekly_counts_Subscriber(filename)
    pprint('{} : {}'.format(city, weekDictSub))
    maxKey = max(weekDictSub, key = weekDictSub.get)
    print('For Subscriber: {} 骑行量最大'.format(maxKey))

    weekDictCus = weekly_counts_Customer(filename)
    pprint('{} : {}'.format(city, weekDictCus))
    maxKey = max(weekDictCus, key = weekDictCus.get)
    print('For Customer: {} 骑行量最大'.format(maxKey))

    weekDictMeanDur = week_mean_duration(filename)
    pprint('{} : {}'.format(city, weekDictMeanDur))
    maxKey = max(weekDictMeanDur, key=weekDictMeanDur.get)
    print('{} 平均骑行时长最大'.format(maxKey))
    print('\r\n')
