import requests
import unittest
from ddt import ddt, data


@ddt
class test_topic_api(unittest.TestCase):
    '''
    接口测试：数据驱动
    '''

    def test_topic(self):
        r = requests.get(url="http://39.107.96.138:3000/api/v1/topics?page=1&tab=ask&limit=1&mdrender=true")
        print(r, type(r))
        # 响应结果 body 文本格式
        text = r.text
        print("text:", type(text), text)
        # 响应结果 body 字典格式
        json = r.json()
        print('json', type(json), json)
        # 响应状态码
        statuscode = r.status_code
        assert statuscode == 200, "状态码应该为200"

        success = json['success']
        assert success, 'success 应该为True'

        # 对data 数据的长度进行断言
        data = json['data']
        assert len(data) == 1, "响应数据应该只有1条"

        for obj in data:
            assert obj['tab'] == 'ask', "tab 值应该为ask"

        # 数据驱动

    testdata = [
        {"limit": 1, "tab": "ask"},
        {"limit": 2, "tab": "share"},
        {"limit": 3, "tab": "job"},
        {"limit": 2, "tab": "good"}
    ]
    url = 'http://39.107.96.138:3000/api/v1/topics'

    @data(*testdata)
    def test_math(self, value):
        url = 'http://39.107.96.138:3000/api/v1/topics'
        print(type(value), value)
        r = requests.get(url, value)
        json = r.json()
        # 响应状态码
        statuscode = r.status_code
        assert statuscode == 200, "状态码应该为200"

        success = json['success']
        assert success, 'success 应该为True'

        # 对data 数据的长度进行断言
        data = json['data']
        assert len(data) == value['limit'], f"响应数据应该只有{value['limit']}条"

        for obj in data:
            assert obj['tab'] == value['tab'], f"tab 值应该为{value['tab']}"


if __name__ == '__main__':
    unittest.main()
