with open('test.txt', 'r+', encoding='utf-8') as f:
    f.seek(1)  # 指定当前指针位置
    print(f.tell())  # 按照字符 读取指针位置
    #print(f.read(4))  #读两个字节
    print(f.tell())  # 按照字符
    f.truncate()#截取当前位置，再保存当前文件


def two_question01():
    num = 0
    for i in range(1,5):
        for j in range(1,5):
            for id in range(1,5):
                if i!=j and i!=id and j!=id:
                    li = [i, j, id]
                    b = [str(n) for n in li]
                    print(''.join(b))
                    num+=1

    print(num)
two_question01()