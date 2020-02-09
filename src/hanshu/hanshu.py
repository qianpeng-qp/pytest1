'''
Created on 2019年7月10日

@author: asus
'''
# 定义函数
def greet_user():
    '''显示问候语'''  #文档注释语
    print("hello")
greet_user()

def greet_user1(name):
    print(name)
greet_user1("lili")
def describe_dog(name,age):
    print(name+str(age))
describe_dog("qqq", 10)
describe_dog(name="bbb", age=20)#关键字实参，确保不会传错

def describe_cat(age,name="dd"):# 注意将默认参数写后面
    print(name+str(age))
describe_cat(age=20)
describe_cat(15,"ss")

#return 返回值
def get_name(first_name,last_name,middle_name=''):      #中间名可以选择
    '''返回完整姓名'''
    full_name=first_name+middle_name+last_name
    return full_name.title()
name=get_name("aaa", "bbb")
print(name)
name =get_name("111", "www", "sss")
print(name)

#返回字典
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
person = build_person("aaa", "bbb")
print(person)

while True:
    print("tell me name:")
    f_name=input("f_name:")
    if f_name =='q':
        break
    l_name=input("l_name:")
    if l_name=='q':
        break
    name = build_person(f_name,l_name)
    print(name)
 #函数中修改列表
def print_modle(up_designs,com_modles):   
    """模拟打印每个设计，直到打印完成，打印完后移到com_modles"""
    while up_designs:
        com_design=up_designs.pop()
        print("print modle:"+com_design)
        com_modles.append(com_design)
        print(up_designs)
def show_modle(com_modles):
    print("all:")
    for modles in com_modles:
        print(modles)
up_designs =['a','b','c']
com_modles=[]
print_modle(up_designs[:], com_modles)      #禁止函数修改列表：
show_modle(com_modles)

#传递任意数量的实参+位置实参
def make_pizza(size,*toppings):
    """打印顾客所有配料+尺寸"""
    print(str(size))
    for topping in toppings:
        print("-"+topping)
make_pizza(12,'aaa')
make_pizza(13,'bbbb','bbbb','ccc')

#使用任意数量关键字实参
def build_pro(first,last,**user_info):
    """创建字典，包含一切用户信息"""
    pro={}
    pro['first_name']=first
    pro['last_name']=last
    for key,value in user_info.items():
        pro[key] =value
    return pro
user_pro = build_pro('a','b',location='ccc',field='ddd')
print(user_pro)



    
    




