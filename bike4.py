# 问题 4c：从骑客量的角度更深入地挖掘骑行时长问题。
# 选择一座城市，研究该城市哪种系统用户的平均骑行时间更长？是会员还是散客？
import csv # 读写 csv 文件

def get_Subscriber_Customer_duration(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        n_subscribers = 0
        n_customers = 0
        sub_minutes = 0.0
        cus_minutes = 0.0

        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
                sub_minutes += float(row['duration'])
            else:
                n_customers += 1
                cus_minutes += float(row['duration'])

        mean_sub_duration = sub_minutes / n_subscribers
        mean_cus_duration = cus_minutes / n_customers
        return (mean_sub_duration, mean_cus_duration)

city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv'}

for city, filename in city_info.items():
    print('{}: {}'.format(city, get_Subscriber_Customer_duration(filename)))
