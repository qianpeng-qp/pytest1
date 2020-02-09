try:
    print(5/0)                            #若此行正确，则跳过ZeroDivisionError；否则执行下方print
except ZeroDivisionError:
    print('wrong')

print("Give me two number,and I'll divide them")
print("Enter 'q' to quit")

while True:                                 #若输入0 则报错
    first_number = input("\n firstnumber: ")
    if first_number == 'q' :
        break
    second_number = input("secondnumber: ")
    try:
        if second_number == 'q':
            break
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You are wrong!")
    else:                                    #依赖于try ，成功执行的代码放到else
        print(answer)

def count_word(filename):
    try:
        with open(filename) as f_ob:
            contents= f_ob.read()
            print(contents)
    except FileNotFoundError:               #文件找不到，则执行下面操作
        #pass                               不做任何提示错误时
        print("wrong")
    else:
        words = contents.split()
        num_words = len(words)
        print(filename+" \n"+str(num_words))

filenames = ['..\doc_1\pi_digits.txt','..\doc_1\programming.txt','sddjakdj.txt']
for folename in filenames:
    count_word(folename)
