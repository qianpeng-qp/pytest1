import csv
'''
解析数据文件
'''

def do_csv(csvpath):
    data = []
    with open(csvpath,mode='r',encoding='utf8') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            print(line)
            data.append(tuple(line))

    return data
print(do_csv('../data/data.csv'))