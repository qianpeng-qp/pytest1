import pytest
'''
函数级别进行测试用例先后执行
'''
@pytest.fixture()
def func(func2,func3):
    '''
    单个测试用例执行前
    :return:
    '''
    print('----func set up---')
    yield
    '''
    单个测试用例执行后
    '''
    print('teardown')

@pytest.fixture(scope='module')
def func2():
    '''
    单个测试用例执行前
    :return:
    '''
    print('----func set up moudle---')
    yield
    '''
    单个测试用例执行后
    '''
    print('teardown')

@pytest.fixture(scope='class')
def func3():
    '''
    单个测试用例执行前
    :return:
    '''
    print('----func set up  class---')
    yield
    '''
    单个测试用例执行后
    '''
    print('teardown class')




def test_01():
    print('tttt')

def test02():
    print('ssss')

class TestTemp2:
    def test1(self,func):
        print('----------------')