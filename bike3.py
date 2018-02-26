#问题 4b：共享单车系统是为短途骑行者而设的。大多数时候，用户在 30 分钟内骑行无需额外付费，
#若是超过该时长，则需支付超时费用。那么，各城市的平均骑行时长是多少？各城市骑行时长超过 30 分钟的比例又是多少？
import csv # 读写 csv 文件

## 使用本框及新框来回答问题 4b。               ##
##                                                                      ##
## 提示：csv 模块会将所有数据读取为字符串，包括数值。 ##
## 因此，在统计数据之前，你需要用函数将字符串转换为      ##
## 合适的数值类型。         ##
## 小贴士：在湾区示例数据中，平均骑行时长为 14 分钟，##
## 骑行时长多于 30 分钟的数据占比 3.5%。                      ##

def mean_time_and_g30_percent(filename):
    """
    本函数会读取一个骑行数据文件，分别报告
    会员、散客和所有系统用户的骑行次数。
    """
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        # 骑行总次数
        n_total = 0
        # 骑行时长多于30分钟的次数
        n_g30 = 0
        # 骑行总的分钟数
        n_total_minutes = 0.0

        # 计算骑行类型
        for row in reader:
            n_total += 1
            duration = float(row['duration'])
            if duration > 30:
                n_g30 += 1
            n_total_minutes += duration

        # 统计平均骑行时长
        mean_time = n_total_minutes / n_total
        # 统计骑行时长多于30分钟的比例
        g30_percent = '{:.1%}'.format(n_g30/n_total)

        # 将结果作为数组返回出来
        return(mean_time, g30_percent)


# data_file = './examples/BayArea-Y3-Summary.csv'
# print(mean_time_and_g30_percent(data_file))

'''
Washington: (18.93287355913721, '10.8%')
Chicago: (16.563629368787335, '8.3%')
NYC: (15.81259299802294, '7.3%')
'''
city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv'}

for city, filename in city_info.items():
    print('{}: {}'.format(city, mean_time_and_g30_percent(filename)))
