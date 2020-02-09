class path_1:
#open()打开文件 传参文件名，返回一个对象
#with在不需要访问时进行关闭，也可以使用closed，但是若程序出错导致文件损坏
    with open('pi_digits.txt') as file_object:
        contens = file_object.read()        #read进行读取所有内容，结尾会多次空行
        print(contens.rstrip())             #rsplit()将结果打印成数组，rstrip()去除空行
        print("--------------------------------------------------")
class path_2:
    with open('test\_test_1.txt') as file_object1:      #  \用于相对路径
        for line in file_object1:            #逐行读取
            print(line.rstrip())
    print("--------------------------------------------------")
class path_3:
    file_path ="D:/ptest.txt"                           # 绝对路径
    with open(file_path, encoding='utf-8') as file_object2:
        lines = file_object2.readlines()  # readlines读取每一行，存储在列表中
        pi_string = ''
        for line in lines:
            print(line.rstrip())
            pi_string += line.strip()     #删除空格
        print(pi_string)
        print(len(pi_string))
        print(pi_string[:52]+".....")       #打印前52位
        birthday = input("输入数字：")
        if birthday in pi_string:
            print("ok")
        else:
            print("wrong")
