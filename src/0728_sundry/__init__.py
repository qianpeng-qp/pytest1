name = input("name: ")
age = input("age： ")
job = input("job： ")

print('Name:' + name + '\nage' + age + '\njob' + job)
print('Name:%s\nAge:%s\nJob:%s' % (name, age, job))  # 只占用一次内存,中文： %s  %（）

message = '''
name:%s
age:%s
job:%s
''' % (name, age, job)
#段落
print(message)
