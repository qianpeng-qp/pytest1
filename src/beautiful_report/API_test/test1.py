import ddt
import unittest

@ddt.ddt
class test1(unittest.TestCase):
    datali=[
        {1,2},
        {2,3}
    ]

    @ddt.data(*datali)
    def testa(self,value):
        print(value)

