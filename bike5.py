#得到最大、最小骑行时间
import csv # 读写 csv 文件

def get_max_duration(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        max_duration = 0.0
        min_duration = 5.01
        for row in reader:
            dur = float(row['duration'])
            if dur > max_duration:
                max_duration = dur
            if dur < min_duration:
                min_duration = dur

        return (max_duration, min_duration)

city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv'}

for city, filename in city_info.items():
    print('{}: {}'.format(city, get_max_duration(filename)))
