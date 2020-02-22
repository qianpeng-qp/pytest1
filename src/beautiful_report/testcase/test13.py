from selenium import webdriver
import unittest

driver = webdriver.Chrome()
class NameTestCase(unittest.TestCase):  # 测试用例
    def test1(self):
        driver.get('https://www.baidu.com/')
        assert driver.current_url == 'https://www.baidu.com/'