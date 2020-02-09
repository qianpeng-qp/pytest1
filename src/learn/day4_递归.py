def cale(n):
    print(n)
    if n / 2 > 1:
        return cale(n / 2)
    print('N:', n)


cale(100)


def cale1(n):
    print(n)
    if n / 2 > 1:
        res = cale1(n / 2)  # res = 10     5=5(res =5)   2.5(res =2.5)  1.25
        print('res:', res)

    print('N:', n)
    return n


cale1(10)

'''斐波那契数列'''


def fun(arg1, arg2, stop):
    if arg1 == 0:
        print(arg1, '\n', arg2)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop:
        fun(arg2, arg3, stop)


'''二分法'''


def binary_search(date_source, find_n):
    mid = int(len(date_source) / 2)
    if len(date_source) >= 1:
        if date_source[mid] > find_n:
            print('data in left of [%s]' % date_source[mid])
            binary_search(date_source[:mid], find_n)
        elif date_source[mid] < find_n:
            print('data in right of [%s]' % date_source[mid])
            binary_search(date_source[mid:], find_n)
        else:
            print('found fin_s', date_source[mid])
    else:
        print('cannot find...')


if __name__ == '__main__':
    date = list(range(1, 60000, 4))
    # print(date)
    binary_search(date, 1)
