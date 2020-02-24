import unittest
from ddt import ddt,data,file_data,unpack


@ddt
class myddt(unittest.TestCase):
    '''测试ddt'''
    @data([2,3],[4,5])
    def test_a(self,value):
        print(value[1])

if __name__=='__main__':
    unittest.main()

