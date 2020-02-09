""""作业：编写登陆接口"""

"""输入用户名密码
认证成功后显示欢迎信息
输错三次后锁定"""

"""3级菜单"""


# # 1、用户信息文件  2、黑名单文件
# class main():
#     with open('blackname.txt') as file_object:
#         blackname = file_object.read()
#     print(blackname)
#     with open('whitename.txt') as file_object1:
#         whitenam = file_object1.read()
#     print(whitenam)


def main():
    count = 0
    while count < 3:
        name = input("用户名： ")
        with open('blackname.txt', 'r') as file_object:
            lines = file_object.readlines()
            blackname2(lines, name)
        if len(name) == 0:
            print('密码不能为空')
            continue

        password = input('密码： ')
        with open('whitename.txt', 'r') as file_object:
            flag = False
            for line in file_object.readlines():
                user, password1 = line.strip().split()
                if name == user and password == password1:
                    print('success!')
                    flag = True
                    break
            if flag == False:
                if count < 2:
                    print('用户名或密码错误')
                count += 1
            else:
                print('成功')


def blackname1(lines, name):
    for line in lines:
        if name == line.strip():
            print('用户 %s 已经被锁定' % name)


def blackname2(lines, name):
    line1 = []
    for line in lines:
        line1.append(line)
    if name in line1:
        print('用户 %s 已经被锁定，退出' % name)

if __name__  == '__main__':
    main()


