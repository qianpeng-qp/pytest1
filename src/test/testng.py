import unittest
from test1 import result

class NameTestCase(unittest.TestCase):  # 测试用例
    def setUp(self):
        pass

    def test_get_result(self):
        params = {'page': 1}
        response = result('get', '/topics', params)
        self.assertEqual(True,response['success'])

    def test_post_result(self):
        params = {'accessToken': '47bac9bd-0c3f-4654-8aaa-171662bd3f45', 'title': 'test11', 'content': 'yyyyy'}
        response = result('post', '/topics', params)
        print(response)
        self.assertEqual('error', response)



    def tearDown(self):
        pass
if __name__ == '__main__':
    NameTestCase