import pytest

data = [('1', '2', '3'), ('2', '2', '3'), ('3', '2', '3')]


@pytest.fixture(params=data, ids=['tab1', 'tab2', 'tab3'])
def func(request):
    '''
    数据传参的时候 主要是作为 不同数据的不同解释
    :param request:  params作为数据驱动
    :return:
    '''
    return request.param


def test_01(func):
    print(f'=========={func}====={type(func)}====={func[0]}')
