import time
from time import strftime
def func():
    starttime = time.perf_counter()
    for x in range(10):
        time.sleep(0.1)
    endtime = time.perf_counter()
    print(f'时间{endtime - starttime}')

def fun1():
    return strftime('%Y_%M_%d',time.localtime())

if __name__ == '__main__':
    print(fun1())
