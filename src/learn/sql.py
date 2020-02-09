import pymysql

connect = pymysql.Connect(host="192.168.0.105", #host="localhost" "127.0.0.1"
                          port=3306,   #端口号
                          user="root",  #用户名
                          passwd="root",  #密码
                          db="test",   #数据库
                          charset='utf8')
cursor = connect.cursor() #定义一个游标，用来执行sql语句
cursor.execute("select * from test")
result = cursor.fetchall() ## fetchone  获取一条  fetchmany 获取多条  fetchall 获取所有
print(result)