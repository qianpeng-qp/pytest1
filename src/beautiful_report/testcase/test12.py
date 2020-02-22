import unittest

class NameTestCase(unittest.TestCase):  # 测试用例
    """测试name_function"""


    def test_first_last_name1(self):
        """能否正确处理janis Joplin"""
        self.assertEqual('22', 'Janis Joplin')  # 断言