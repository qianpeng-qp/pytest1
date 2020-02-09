name = int(1)
print(type(name))
'''int常用方法'''
age = -18
print(age.__abs__())  # 绝对值
print(age.__add__(100))
print(age.__bool__())  # 返回布尔
print(type(age))
print(type(age.__float__()))  # 转换成浮点类型

print(age.__floordiv__(6))  # 地板除
print(age.__ge__(8))

all_item = 95
pager = 10
result = all_item.__divmod__(pager)
print(result)  # (9,5)  9余5  除法
result1 = all_item.__rdivmod__(pager)
print(result1)

'''str常用方法'''
name = 'hello'
print(type(name))  # 获取类
print(dir(name))  # 获取成员

result = name.__contains__('llo')  # 是否包含
result = name.capitalize()  # 首字母大写
result = name.casefold()  # 小写
result = name.center(20, '*')  # 字符位置
result = name.count('l')  # 字符出现次数
result = name.encode('GBK')  # 转换编码格式
result = name.endswith('e', 0, 2)
print(result)

name1 = '\talex'
print(len(name1))
result = name1.expandtabs()  # TAB转换成空格
print(result)
print(len(result))

result = name1.find('a')  # 查找a位置
result = name1.index('a')
print(result)

name = 'alex {0}  as {1}'
result = name.format('sb', 'eric')  # 字符串的拼接0
li = ['1', '2', '3']

print(result)
result = '_'.join(li)  # 序列拼接_ 可以为空
print(result)

# #转换，需要先做一个对应表，最后一个表示删除字符集合
# intab = "aeiou"
# outtab = "12345"
# trantab = maketrans(intab, outtab)
# str = "this is string example....wow!!!"
# str.translate(trantab, 'xm')

name = 'alexissb'
result = name.partition('is')  # 以is切分
print(result)

print(name.replace('s', 'o', 1))

print(name.split())  # 分割
print(name.swapcase())  # 大小写转换

'''list常用方法'''
list1 = [i for i in range(10)]
print(list1)
list1.extend((11, 22, 22,))
print(list1)

list1.insert(0, 33)  # 指定下标插入
print(list1)

print(list1.pop(0))  # 打印删除的0位置的值
print(list1)

list1.remove(22)  # 去除第一个22
print(list1)

list1.reverse()  # 列表反转
print(list1)

'''元组常用方法'''
l1 = [11, 22, 33,]
tu1 = tuple(l1)  # 列表转换成元组
print(tu1)

tu = (11, 22, 33,)  #元组转列表
l2 = list(tu)
print(l2)

'''字典常用方法'''
dic = {'k1':'k2'}
dic = dict(k1 = 'k2',k2 = 'k3')
print(dic.fromkeys(['k1','k2','k3'],'v1'))
print(dic.get('k4','alex'))
dic.pop('k1')  #删除指定值
print(dic)
dic.setdefault('k1')  #设置值
print(dic)
ret = dic.update({'k3':123})  #更新值
print(dic)
favorite_language = {
    'jen': ['python', 'ruby'],
    'mike': 'java',
    'phil': ['c', 'java'],
    'tom': ['python', 'haskill']
}
for name, language in favorite_language.items():
    print(name.title(),language)

#{'k1':[66,77,88,99],'k2}:[11,22,33,44,55]
def test():
    dic ={}
    all_list = [11,22,33,44,55,66,77,88,99,]
    for i in all_list :
        if i>66 :
            if 'k1' in dic.keys():
                dic['k1'].append(i)
            else:
                dic['k1'] = [i,]
        else:
            if 'k2' in dic.keys():
                dic['k2'].append(i)
            else:
                dic['k2']=[i, ]
    print(dic)

if __name__ == '__main__':
    test()
