import math
import csv
from pprint import pprint # 用于输出字典等数据结构
'''
一天内的哪个时候系统使用最频繁？
会员和散客的使用模式有区别吗？
'''
def hour_counts(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theHourDict = {
        '1':0, '2':0, '3':0, '4':0, '5':0, '6':0,
        '7':0, '8':0, '9':0, '10':0, '11':0, '12':0,
        '13':0, '14':0, '15':0, '16':0, '17':0, '18':0,
        '19':0, '20':0, '21':0, '22':0, '23':0, '0':0,
        }
        for row in reader:
            theHourDict[row['hour']] += 1

        return theHourDict

def hour_counts_Subscriber(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theHourDict = {
        '1':0, '2':0, '3':0, '4':0, '5':0, '6':0,
        '7':0, '8':0, '9':0, '10':0, '11':0, '12':0,
        '13':0, '14':0, '15':0, '16':0, '17':0, '18':0,
        '19':0, '20':0, '21':0, '22':0, '23':0, '0':0,
        }
        for row in reader:
            if row['user_type'] == 'Subscriber':
                theHourDict[row['hour']] += 1

        return theHourDict

def hour_counts_Customer(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theHourDict = {
        '1':0, '2':0, '3':0, '4':0, '5':0, '6':0,
        '7':0, '8':0, '9':0, '10':0, '11':0, '12':0,
        '13':0, '14':0, '15':0, '16':0, '17':0, '18':0,
        '19':0, '20':0, '21':0, '22':0, '23':0, '0':0,
        }
        for row in reader:
            if row['user_type'] == 'Customer':
                theHourDict[row['hour']] += 1

        return theHourDict

# Do some test.
city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv'}
for city, filename in city_info.items():
    #hourDict = hour_counts(filename)
    #hourDict = hour_counts_Subscriber(filename)
    hourDict = hour_counts_Customer(filename)
    print(city + ":\r\n")
    print(hourDict)
    maxKey = max(hourDict, key = hourDict.get)
    print('{}点的时候，系统使用最频繁'.format(maxKey))
    minKey = min(hourDict, key = hourDict.get)
    print('{}点的时候，系统使用最不频繁'.format(minKey))
