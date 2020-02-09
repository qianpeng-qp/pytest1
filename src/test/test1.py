import requests


# url1 = 'http://39.107.96.138:3000/api/v1{}'
# url2 = '/topics'
# url = url1.format(url2)
# response = requests.get(url=url)
# if response.status_code == 200:
#     print(response.text)
# else:
#     print('error')

def result(type1, url2, params):
    url1 = 'http://39.107.96.138:3000/api/v1{}'
    url = url1.format(url2)
    print(url)
    if type1 == 'get':
        response = requests.get(url, params)
        if response.status_code == 200:
            # print(response.text)
            return response.json()
        else:
            print('error')
            return 'error'
    elif type1 == 'post':
        response = requests.post(url, data=params)
        if response.status_code == 200:
            # print(response.text)
            return response.json()
        else:
            #print(response.text)
            return 'error'


if __name__ == '__main__':
    params = {'page': 1}
    print(result('get', '/topics', params))
    params = {'accessToken': 'c9715651-0d4a-4c50-af79-7fac08110e2a', 'title': 'test11', 'content': 'yyyyy'}
    print(result('post', '/topics', params))
