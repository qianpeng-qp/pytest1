def show1(**arg):  # 字典
    print(arg, type(arg))


show1(n1=78)


def show2(*arg):  # 元组
    print(arg, type(arg))


show2(78)


def show3(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


show3(11, 22, 33, 44, n=1, m=3)
l = [11, 22, 33, 44]
d = {'n': 1, 'm': 3}
show3(l, d)  # l和d做为一个整体
show3(*l, **d)  # 使用*区分，两*字典

s1 = '{0} is {1}'
# result = s1.format('alex','zb')
l = ['alex', '2b']
result = s1.format(*l)  # 使用*区分
print(result)

s2 = '{name} is {acter}'
# result = s2.format(name='alex', acter='sb')
d = {'name': 'alex', 'acter': 'sb'}
result = s2.format(**d)
print(result)

func = lambda a: a + 1  # 创建函数a，并函数内容a+1 并返回结果
ret = func(99)
print(ret)
