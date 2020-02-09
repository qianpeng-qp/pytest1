'''二维数组,将数组旋转'''

'''
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]

---------------------------
[0, 0, 0, 0]
[1, 1, 1, 1]
[2, 2, 2, 2]
[3, 3, 3, 3]
'''
data = [[col for col in range(4)] for row in range(4)]
print(data)
print('-----------------------------')
for row in data:
    print(row)

print('--------------------------------')

for r_index, row in enumerate(data):
    # print(row)
    for c_index in range(r_index, len(row)):
        tem = data[c_index][r_index]
        data[c_index][r_index] = row[c_index]
        data[r_index][c_index] = tem

for i in data:
    print(i)

'''正则'''
import re

m = ('abc', 'abcf')
m = re.match('[0-9][0-9]', '75abcf')
m = re.match('[0-9]{0,10}', '75abcf')  # 0-10次
m = re.match('[0-9]{10}', '75abcf')  # 10次
m = re.findall('[0-9]{1,10}', '75ab9cf')  # 自己直接返回匹配的值
m = re.findall('[a-zA-Z]{1,10}', '75ab9cf')  # 匹配所有字母
m = re.findall('.*', '75ab9cf')  # 匹配所有
m = re.findall('.+', '75ab9cf')  # 匹配一个不包含0
m = re.findall('[a-zA-Z]+', '75a.b_9cf')  # 匹配字母
m = re.findall('~', '75a. b_9cf')
m = re.search('\d+$', 'ss75a. b_9cf')  #整个查找  全部数字
#m= re.sub('^\d+','|','ss75a. b_9c1f',count=2)   #替换两个

if m:
    print(m)
    #m.
