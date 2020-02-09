filename = 'programming.txt'
with open(filename,'w') as file_object:             #覆盖得写
    file_object.write("sa\n")
    file_object.write("sjdsfaj\n")
with open(filename,'a') as file_object:             #末尾添加
    file_object.write('aaaaaa\n')
    file_object.write('bbbbbbb\n')
with open('programming.txt') as file_object:
    contens = file_object.read()                    #读
    print(contens.rstrip())
