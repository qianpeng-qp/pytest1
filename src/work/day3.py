import json

with open('haproxy.cfg','r',encoding='utf-8') as f:
    list_1=list(f.readlines())
    print(list_1)
#{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}
json1 = input('输入：')
def re(json1):
    dic_1 = json.loads(json1)
    dic_2 = 'server %s %s weight%s maxconn%s'%(dic_1['record']['server'],dic_1['record']['server'],dic_1['record']['weight'],dic_1['record']['maxconn'])
    return dic_2
print(re(json1))




