import unittest
from BeautifulReport import BeautifulReport    #导入BeautifulReport




if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('testcase/', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')
    #log_path='.'把report放到当前目录下