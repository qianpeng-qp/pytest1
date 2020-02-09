import unittest

from testcase.name_function import get_formatted_name,AnoymoisSurey
print("Enter 'q' at any time to quit" )
while True:
    first = input("first: ")
    if first == 'q':
        break
    last = input("last: ")
    if last  == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print('formatted_name:\t' + formatted_name)

question= "What are you learn?"         #定义问题，创建对象
my_surver = AnoymoisSurey(question)
my_surver.show_question()
print("Enter 'q' at any time to quit")
while True:
    response = input("result: ")
    if response == 'q':
        break
    my_surver.store_response(response)
print("显示结果：")
my_surver.show_results()