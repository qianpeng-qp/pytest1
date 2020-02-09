import json
numbers = [2,3,4,5,11,13]
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)        #json.dump 存储这组数字

with open(filename) as f_obj:
    numbers = json.load(f_obj)       #json.load 将json存储到内存，可以使用
print(numbers)

#如果已有用户名，则读取，否则写入
filename1 = 'username1.json'
# username = input("输入姓名：")
# with open(filename1, 'w') as f_obj1:  # 存储到json文件
#     json.dump(username, f_obj1)
#     print("remember:"+username)
# with open(filename1) as f_obj2:  # 存储到内存并读取
#     username = json.load(f_obj2)
#     print(" user_naem :" + username)
def greet_user():
    """问候用户并指出名字"""
    try:
        with open(filename1) as f_obj2:  # 存储到内存并读取
            username = json.load(f_obj2)
    except FileNotFoundError:
        username = input("输入姓名：")
        with open(filename1, 'w') as f_obj1:  # 存储到json文件
            json.dump(username, f_obj1)
            print("remember:"+username)
    else:
        print(" user_naem :" + username)
greet_user()

def get_stored_username():
    """如果存储了姓名就打出"""
    try:
        with open(filename1) as f_obj2:  # 存储到内存并读取
            username = json.load(f_obj2)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示输入新用户名"""
    username = input("输入姓名：")
    with open(filename1, 'w') as f_obj1:  # 存储到json文件
        json.dump(username, f_obj1)
        print("remember:" + username)

def greet_user():
    """问候用户并指出名字"""
    username = get_stored_username()
    if username:
        print("welcome"+ username)
    else:
       username = get_new_username()
greet_user()