import csv

def get_duration_list(filename):
    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)

        aList = []
        for row in reader:
            aList.append(float(row['duration']))

        return aList

city_info = {'Washington': './data/Washington-2016-Summary_my.csv',
             'Chicago': './data/Chicago-2016-Summary_my.csv',
             'NYC': './data/NYC-2016-Summary_my.csv'}

for city, filename in city_info.items():
    durList = get_duration_list(filename)
    print('{} last line duration: {}'.format(city, durList[-1]))
