print(abs(-99.9))  # 绝对值
print(all([1, 2, 3, '']))  # 所有必须不为空，才真
print(any([1, 2, 3, '', None]))  # 有一个真则为真
print(ascii(8))  # 自动执行__repr__方法
print(bin(10))  # 转换二进制
print(bool(None))  # 布尔 返回false
print(bytearray('五五', encoding='utf-8'))  # 转成字节数组
print(bytes('五五', encoding='utf-8'))  # 转成字符串
print(callable(lambda x: x + 1))  # 是否可以执行
print(chr(99))  # 将数字码转换成字符
print(ord('c'))  # 将字符转换成数字 ：验证码
print(divmod(5, 2))  # 商和余数
for i in enumerate(['alex', 'eric'], 3):
    print(i)  # 加上序列
print(eval('6*8'))  # 字符串两个数相乘6*8
li = [11, 22, 33, 44]
print(list(map(lambda x: x + 100, li)))  # map循环调用lambda x: x + 100或者调用方法


def func(x):
    if x > 33:
        return True
    else:
        return False


print(list(filter(func, li)))  # 根据True条件返回值,过滤
''''
format()# 类似形参，传参数
float()#浮点
frozenset()#不能修改的set
hex(100) #16进制
oct()#8进制
range(0,10) #区间
round(9.8) #四舍五入
max(11,22,33) # 最大
min(11,22,33)  #最小
sum(11,22)#求和
super #子类用父类
'''''
x = [11, 22, 33, 44]
y = [22, 33, 44, 55]
print(list(zip(x, y)))  # xy相拼
