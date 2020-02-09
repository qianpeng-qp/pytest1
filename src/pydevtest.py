# from nt import remove
# from audioop import reverse
from idlelib.colorizer import color_config

message = "hello world"
print(message)
print(message.title())
# 首字母大写
print(message.upper() + " " + message.lower())
# 大小写
print("\t age \n")
# t换行 \n空格
language = ' python '
print(language.rstrip())
# 去后面除空吧
print(language.lstrip())
# 去前面除空吧
print(language.strip())
# 去两端
print(1 + 2)
age = 25
message = "happy" + str(age) + "day"
# int转string
print(message)

shuzu = [1, 2, 3, 4, 'sajsdak']
print(shuzu)
print(shuzu[4])

print(language + shuzu[4].title())

shuzu[2] = 'saj ajsd'
print(shuzu[2])
# 修改

shuzu.append('jskal ;')
# appened 末尾添加
print(shuzu)

print(shuzu.index(4))

shuzu.insert(1, 'klasd')
print(shuzu)
# insert 从xx位置添加

del shuzu[0]
# 删除XX位置
print(shuzu)

pop = shuzu.pop(2)  # 删除末尾
print(shuzu)
print(pop)

shuzu.remove(2)  # 删除值
print(shuzu)

shuzu.insert(3, 'ttt')
a = 'ttt'
print(shuzu)
shuzu.remove(a)
print(shuzu)

shuzu[1] = 'waas'
shuzu.sort()  # 永久性排序
print(shuzu)
shuzu.sort(reverse=True)  # 倒叙永久
print(shuzu)

print(shuzu.count('4'))

# 函数sorted
print(sorted(shuzu))  # 非永久正序    

shuzu.reverse()  # 倒着打印
print(shuzu)
print(len(shuzu))  # 数组长度

# for循环-----------------------------------------------------------------------------
for shu in shuzu:  # 定义shu 打印数组 循环
    print("lalalal\t" + shu.title())
print("hello world")

# unexpected indent 不必要的缩进  expected an indented block 应要缩进

for value in range(1, 5):  # range生产数字 1到4 不会包含5
    print(value)
number = list(range(1, 5))  # list 数字转换列表
print(number)
even_number = list(range(1, 10, 2))  # range 指定步长
print(even_number)

square = []
for value in range(1, 5):
    square = value ** 2  # ** 平方
    print(square)
square1 = []
for value in range(1, 5):
    # square1 = value**2
    square1.append(value ** 2)
print(square1)

print(min(square1) + max(square1) + sum(square1))

square2 = [value ** 2 for value in range(1, 5)]  # 缩写
print(square2)

number1 = [value for value in range(1, 5)]
print(sum(number1))

print(square2[0:3])  # 切片 0到3位
print(square)
print(square2[:3])

# 遍历
for value in square2[0:2]:
    print(value)

square3 = square2[:]
print(square3)
square2.append(29)
square3.append(22)
print(square2)
print(square3)

number2 = (1, 2)
# number2[0] = 3  报错 无法修改元组的值
print(number2[0])
print(number2[1])

number2 = (3, 4)  # 再次赋值
print(number2[0])
print(number2[1])

# tuple(number)   元组转列表

# if语句------------------------------------------------------------------------------
print(square1)
for value in square1:
    if value == 4:  # == 为相等 ！=为不等
        print(value)
    else:
        print("ll")
for value in square1:
    if value >= 9 and value <= 10:  # and 为并列 or为或者
        print(value)
    else:
        print(0)
if 5 not in square1:  # not in 特定值不在数组中
    print("shi")
print((3, 4) == number2)  # 打印布尔类型  number2 =(3,4)

number = 19
if number >= 18:
    print("大于18")
elif number == 18:
    print("等于18")  # elif 多个使用,可以省略else
else:
    print("小于18")

if 4 in square1:
    print("ye")  # if 可以多个使用
if 9 in square1:
    print("o ye")

if 4 in square1:
    print("不打印9")
elif 9 in square1:  # if通过不运行elif
    print("o ye")

for value in square1:
    if value == 9:
        print("打酒")  # 检查特殊元素
    else:
        print(value)
square = [1, 2]
if square:
    print("非空")
else:
    print("空")
for value in square:
    if value in square1:  # 判断数组1的值在数组2中么
        print("有")
    else:
        print("空")
# 字典值-------------------------------------------------------------------------------
dog_0 = {'color': 'black', 'points': 1}  # {} 键值
print(dog_0['color'])
print(dog_0['points'])
print("打印" + dog_0['color'])  # str和int不能相加
print("打印" + str(dog_0['points']))  # 强制转换
print(dog_0)
dog_0['name'] = 'tt'  # 添加键值
dog_0['age'] = 'dd'
print(dog_0)

dog_1 = {}
dog_1['color'] = 'red'
dog_1['age'] = 2
print(dog_1)
dog_1['color'] = 'green'
print(dog_1)
# 键值的更新
alien_0 = {'x_position': 0, 'y_position': 0, 'speed': 'medium'}
print("初始位置:" + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("此时位置:" + str(alien_0['x_position']))

# del必须指定字典名和要删除的键名
del dog_0['color']
print(dog_0)
# 遍历所有的键-值对
favorite_language = {
    'jen': 'python',
    'mike': 'java',
    'phil': 'c',
    'tom': 'python',
}
print("jen \t" + favorite_language['jen'])
for name, language in favorite_language.items():  # items 返回一个键和一个值
    print("name:" + name + "languare :" + language)

for name in favorite_language.keys():  # 获取所有的键， 可以去除keys 输出不变
    print(name)
friends = ['tom', 'mike']
for name in favorite_language.keys():
    if name in friends:
        print(name + "\t" + language)

# 按顺序遍历所有值
for name in sorted(favorite_language, reverse=False):
    print(name)
# 遍历字典中的所有值 valus(),set去重
for language in set(favorite_language.values()):
    print(language)
dog_2 = {'coloe': 'black', 'age': 2}
dogs = [dog_0, dog_1, dog_2]
for dog in dogs:
    print(dog)

dogs = []
for dog_nymber in range(30):  # 创建30个字典
    new_dog = {'color': 'red', 'age': 3}
    dogs.append(new_dog)
print(str(len(dogs)))  # 打印30个
for dog in dogs[0:3]:
    if dog['color'] == 'red':
        dog['color'] = 'yellow'  # 增加键和值
        dog['speed'] = 'medium'
for dog in dogs[:5]:  # 打印前5个
    print(dog)
# 字典中存储列表
favorite_language = {
    'jen': ['python', 'ruby'],
    'mike': 'java',
    'phil': ['c', 'java'],
    'tom': ['python', 'haskill']
}
for name, language in favorite_language.items():
    print(name.title() + ':')
    for language_1 in language:
        print(language_1.title())

users = {
    'user1': {
        'name': 'alien',
        'age': 4,
        'location': 'aaa'
    },
    'user2': {
        'name': 'blown',
        'age': 5,
        'location': 'bbb'
    },
    'user3': {
        'name': 'mike',
        'age': 6,
        'location': 'ccc'
    }
}
for user_name, users_info in users.items():
    print('name:' + user_name + '\t age:' + str(users_info['age']) + '\tlocation:' + users_info['location'])
