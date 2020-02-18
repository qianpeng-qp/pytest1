"""
文件以test_开始 或者 以 _test结尾的py  (test不区分大小写)

"""

def test_l():

    """ test开始的函数会被当做测试用例直接执行"""
    assert True

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5