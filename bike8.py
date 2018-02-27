import csv
from pprint import pprint # 用于输出字典等数据结构
'''
不同月份或季度的骑客量有什么区别？
哪个月份/季度的骑客量最高？
会员骑行量与散客骑行量之比会受月份或季度的影响吗？
'''
#得到每个月的骑客量
def month_counts(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theMonthDict = {
        '1':0, '2':0, '3':0, '4':0, '5':0, '6':0,
        '7':0, '8':0, '9':0, '10':0, '11':0, '12':0,
        }
        for row in reader:
            theMonthDict[row['month']] += 1

        return theMonthDict

#得到每个季度的骑客量
def quarter_counts(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theQuarterDict = {
        '1':0, '2':0, '3':0, '4':0
        }
        for row in reader:
            if row['month'] == '1' or row['month'] == '2' or row['month'] == '3':
                theQuarterDict['1'] += 1
            if row['month'] == '4' or row['month'] == '5' or row['month'] == '6':
                theQuarterDict['2'] += 1
            if row['month'] == '7' or row['month'] == '8' or row['month'] == '9':
                theQuarterDict['3'] += 1
            if row['month'] == '10' or row['month'] == '11' or row['month'] == '12':
                theQuarterDict['4'] += 1
        return theQuarterDict

#得到会员骑行量与散客骑行量
def month_counts_ratio(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        theMonthDict = {
        '1':{'Subscriber':0, 'Customer':0}, '2':{'Subscriber':0, 'Customer':0},
        '3':{'Subscriber':0, 'Customer':0}, '4':{'Subscriber':0, 'Customer':0},
        '5':{'Subscriber':0, 'Customer':0}, '6':{'Subscriber':0, 'Customer':0},
        '7':{'Subscriber':0, 'Customer':0}, '8':{'Subscriber':0, 'Customer':0},
        '9':{'Subscriber':0, 'Customer':0}, '10':{'Subscriber':0, 'Customer':0},
        '11':{'Subscriber':0, 'Customer':0}, '12':{'Subscriber':0, 'Customer':0}
        }
        for row in reader:
            if row['user_type'] == 'Subscriber':
                theMonthDict[row['month']]['Subscriber'] += 1
            elif row['user_type'] == 'Customer':
                theMonthDict[row['month']]['Customer'] += 1
        return theMonthDict

# Do some test.
city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv'}
for city, filename in city_info.items():
    aDict = month_counts(filename)
    pprint('{} : {}'.format(city, aDict))
    maxKey = max(aDict, key = aDict.get)
    print('{}月骑客量最高'.format(maxKey))

    quarter_dict = {}
    quarter_dict['1'] = int(aDict['1']) + int(aDict['2']) + int(aDict['3'])
    quarter_dict['2'] = int(aDict['4']) + int(aDict['5']) + int(aDict['6'])
    quarter_dict['3'] = int(aDict['7']) + int(aDict['8']) + int(aDict['9'])
    quarter_dict['4'] = int(aDict['10']) + int(aDict['11']) + int(aDict['12'])
    pprint(quarter_dict)
    maxKey = max(quarter_dict, key = quarter_dict.get)
    print('{}季度骑客量最高'.format(maxKey))

    aDict = month_counts_ratio(filename)
    pprint(aDict)
    radio = {}
    for key, sc in aDict.items():
        radio[key] = sc['Subscriber'] / sc['Customer']
    pprint(radio)
    maxKey = max(radio, key = radio.get)
    print('{}月会员与散客的比率最高'.format(maxKey))
    print('\r\n')
