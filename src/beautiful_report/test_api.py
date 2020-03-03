import unittest
from BeautifulReport import BeautifulReport    #导入BeautifulReport
from testapi import test_topic_api




if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('testcase/', pattern='test*.py')
    test_suite.addTest(test_topic_api('test_topic'))
    test_suite.addTest(test_topic_api('test_new_topic'))
    #test_suite.addTest(test_topic_api('test_math'))
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')
    #log_path='.'把report放到当前目录下