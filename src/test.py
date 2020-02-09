#input 控制台输入
from multiprocessing import active_children
from _ast import Num

message_1 ="print"
message_1 +=": "
message = input(message_1)
print(message)

age = input("how old are you ?")  
age = int(age)#input为str类型，转换成int
print(age>=18)

double_1 =input("输入数字")
double_1 = int(double_1)
if double_1%2 == 0:
    print("双数")
else: 
    print("单数")
    
    

    
#while 循环---------------------------------------------------------------------------
number1 = 1
while number1 <=5:
    print(number1)
    number1 +=1
#选择quit退出
message =""
active = True
while active:  #定义true
        message = input("prompt:")
        if message =="quit":
            break       #退出循环
#            active = False
        else:
            print(message)

number = 0
while number <10:
    number +=1
    if number %2 ==0:
        continue #不再执行下方语句
    print(number)

users = ['alean' , 'mike' ,'dancy']
users_1 = []
while users:
    user_info = users.pop()
    print("修改："+user_info)
    users_1.append(user_info)

for user in users_1:
    print(user)
    
pets =['dog','cat','rabit','cat','goldfish','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#用户输入补充字典值
responses ={}
while True:
    name = input("name:")
    response = input("结果:")
    responses[name]=name
    responses[response]=response
    repeat = input("继续？：")
    if repeat =='quit':
        break
print('result: ')
for name,response in responses.items():
    print(name +" \n"+ response)