name = iter(['alex', 'jack', 'lisa'])  # 迭代器 使用next每次取一个数
print(name)
print(name.__next__())
print(name.__next__())
print(name.__next__())


# 生成器
def cash_money(amount):
    while amount > 0:
        amount -= 100
        yield 100
        print('又来取钱了')


atm = cash_money(500)  # 函数是生成器，返回迭代器，调用使用__next__
print(type(atm))
print(atm.__next__())
print(atm.__next__())
print('大保健')
print(atm.__next__())
print(atm.__next__())

# 异步
import time


def consumer(name):
    print('%s is 准备吃包子' % name)
    while True:
        baozi = yield
        print('包子%s来了,被%s吃了' % (baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('开始做包子')
    for i in range(10):
        #        time.sleep(1)
        print('做了2个包子')
        c.send(i)  # 将值发送给yield
        c2.send(i)


producer('alex')
