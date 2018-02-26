from datetime import datetime # 日期解析操作
from pprint import pprint

pprint(datetime.now())

theDateTime = '1/1/2016 00:09:55'
theFormat = '%m/%d/%Y %H:%M:%S'
dt = datetime.strptime(theDateTime, theFormat)
print(dt)
print(dt.year)
print(dt.month)
print(dt.isoweekday())
print(dt.strftime('%A'))
