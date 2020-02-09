import unittest

from testcase.name_function import get_formatted_name, AnoymoisSurey


class NameTestCase(unittest.TestCase):  # 测试用例
    """测试name_function"""

    def test_first_last_name1(self):
        """能否正确处理janis Joplin"""
        formatted_name = get_formatted_name('janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')  # 断言

    def test_first_last_middle_name(self):
        """能否正确处理像Wolfgang Amadeus Mozart"""
        formatted_name = get_formatted_name('Wolfgang', 'Mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


class AnoymoisSureyTestCase(unittest.TestCase):
    """针对AnoymoisSurey测试"""

    def test_response(self):
        """测试答案是否存储"""
        question = "What are you learn?"
        my_survey = AnoymoisSurey(question)
        responses = ['English', 'Chinese']  # 存储多个答案
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

    def setUp(self):
        question = "What are you learn?"
        self.my_survey = AnoymoisSurey(question)
        self.responses = ['English', 'Chinese']  # 存储多个答案

    def test_store_sigle(self):
            """测试单个答案"""
            self.my_survey.store_response(self.responses[0])
            self.assertIn(self.responses[0], self.my_survey.responses)

    def test_two_sigle(self):
        """测试三个是否正常存储"""

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
