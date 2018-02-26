import csv # 读写 csv 文件

def number_of_trips(filename):
    """
    本函数会读取一个骑行数据文件，分别报告
    会员、散客和所有系统用户的骑行次数。
    """
    with open(filename, 'r') as f_in:
        # 设置 csv reader 对象
        reader = csv.DictReader(f_in)

        # 初始化计数变量
        n_subscribers = 0
        n_customers = 0

        # 计算骑行类型
        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
            else:
                n_customers += 1

        # 统计骑行总次数
        n_total = n_subscribers + n_customers

        # 将结果作为数组返回出来
        return(n_subscribers, n_customers, n_total)

## 修改此框及上框，回答问题 4a。##
## 记得运行你在问题 3 中创建的数据文件清理函数。     ##

# data_file = './examples/BayArea-Y3-Summary.csv'
# print(number_of_trips(data_file))
city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv',
             'BayArea': './examples/BayArea-Y3-Summary.csv'}

for city, filename in city_info.items():
    print('{}: {}'.format(city, number_of_trips(filename)))
