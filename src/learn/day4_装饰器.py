def login(func):
    def inner(*arg, **kwargs):
        print('passed user version...')
        return func(*arg, **kwargs)

    return inner


# 无参数的，返回内存地址。不调用tv
@login
def home_page(name):
    print('Welcome %s to home page' % name)


@login
def tv(name, password=123):
    print('Welcome %s to TV page' % name)
    return 4


@login
def movie(name):
    print('Welcome %s to MOVIE page' % name)


# tv = login(tv)
tv('alex', password=456)
print(tv)
movie('alex')


# !/usr/bin/env python
# coding:utf-8

def Before(request, kargs):
    print('before')


def After(request, kargs):
    print('after')


def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):
            before_func(request, kargs)

            main_func(request, kargs)

            after_func(request, kargs)

        return wrapper

    return outer


@Filter(Before, After)
def Index(request, kargs):
    print('index')


Index('rpr', 'alex')


def w1(main_func):
    def outer1(request, kargs):
        print('before1')
        main_func(request, kargs)
        print('after1')
    return outer1


@w1
def show(request, kargs):
    print('show1')

#执行w1,把自己装饰的函数的函数名作为参数，w1(show)
#show函数重新定义，w1(show)返回值
#新show = def outer1(request, kargs)

show('rpr', 'alex')