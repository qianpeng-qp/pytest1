s1 = set()  # 防止重复
s1.add('alex')  # 添加
print(s1)
s1.add('alex')
print(s1)

s2 = s1.copy()  # 复制
print(s2)

s3 = set(['alex', 'eric', 'tony', 'alex'])  # 列表自动去重
print(s3)

s4 = s3.difference(['alex', 'eric'])
print(s4)  # 打印不同的值

s4 = s3.difference_update(['alex', 'eric'])

ret = s3.pop()
print(s3)

old_dict = {
    "#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#2": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#3": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80}
}

# cmdb 新汇报的数据
new_dict = {
    "#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 800},
    "#3": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#4": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80}
}
'''要old_dict要更新的数据'''
# 交集：要更新的数据
old = set(old_dict.keys())
new = set(new_dict.keys())
update_set = old.intersection(new)
print(update_set)
# 差集：原来要更新的
delete_set = old.symmetric_difference(update_set)  # 要删除的集合
# delete_set = old.difference(update_set)
print(delete_set)

add_set = new.symmetric_difference(update_set)  # 要添加的集合
print(add_set)

# 比较difference 和symmetric_difference差异
s1 = set([11, 22, 33])
s2 = set([22, 44])
ret1 = s1.difference(s2)  # 单边的差别
ret2 = s1.symmetric_difference(s2)  # 两边的差别
print(ret1)
print(ret2)

from collections import Counter

obj1 = Counter('aaaabbbasbdasbdabdasbdadsb,b')  # 计数器
print(obj1)

ret = obj1.most_common(4)  # 打印最多的4位
print(ret)

t = [k for k in obj1.elements()]  # 获取所有元素
print(t)

for k, v in obj1.items():
    print(k, v)

obj = Counter(['11', '22', '33'])
print(obj)
obj.update(['eric', '11', '11'])
print(obj)
obj.subtract(['eric', '11', '11'])

# 有序字典

from collections import OrderedDict

dic = OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'k3'
dic.setdefault('k4', '66')  # 默认值
print(dic)

# dic.move_to_end('k1') #移动
# print(dic)

dic.popitem()  # 后进先出，取最后一个
print(dic)

dic.update({'k1': 'v111', 'k10': 'v10'})
print(dic)

# 默认字典
from collections import defaultdict

my_dict = defaultdict(list)
my_dict['k1'].append('v1')
print(my_dict)

b = []
a = [4, 1, 2, 6, 5, 7]
for i in a:
    if not b:
        b.append(i)
    if i > b[-1]:
        b.append(i)
print(b)

# 可命名元组
from collections import namedtuple

Mytuple = namedtuple('Mytuple', ['x', 'y', 'c'])
obj = Mytuple(11, 22, 33)
print(obj.x)
print(obj.y)
print(obj.c)

# 双向队列
from collections import deque

d = deque()
d.append('1')
d.appendleft('10')  # 左边添加
d.appendleft('1')
r = d.count('1')  # 1的个数
print(d)
print(r)
d.extend(['22', '33', '33'])
d.extendleft(['22', '33', '33'])
print(d)
d.rotate(1)  # 尾部拿数据插前面
print(d)

# 单向队列
import queue

q = queue.Queue()
q.put('123')    #放入先进先出原则
q.put('456')
q.put('789')
print(q.qsize())  #返回队列元素个数
print(q)
print(q.get())

#深浅拷贝

import copy

a1 = 123456
# b1 = 123456
a2 = a1  # 赋值
print(id(a1))
print(id(a2))

a3 = copy.deepcopy(a1)
print(id(a3))  # copy和deepcoopy一致

# 其他元组、字典等
n1 = {'k1': 'w1', 'k2': 123, 'k3': ['alex', 123456]}
n2 = copy.copy(n1)  #浅拷贝，只会拷一层，嵌套多层的则不会拷
print(id(n1['k3']))
print(id(n2['k3']))

print(id(n1))
n3 = copy.deepcopy(n1)  #深拷贝，全都会拷贝
print(id(n3))

dic = {
    'cpu':[80,],
    'mem':[80,],
    'disk':[80,]
}
print(dic)
new_dic = copy.deepcopy(dic)
new_dic['cpu'][0] = 50  #浅拷贝，修改拷贝后的内容时会使原数据也改变
print('before',dic)
print(new_dic)


print(new_dic.keys())

for i in new_dic.keys():
    print(i)

