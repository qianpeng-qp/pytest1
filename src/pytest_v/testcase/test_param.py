import pytest

@pytest.fixture(params=[0,1])
def func(request):
    return request.param

def test_01(func):
    print(f'=========={func}')