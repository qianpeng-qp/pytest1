'''1、用户输入一个数值，请判断用户输入的是否为偶数？
是偶数输出True,不是输出False（提示:input输入的不管是什么，
都会被转换成字符串，自己扩展，想办法将字符串转换为数值类型，再做判段）'''

# class print_num() :
#     num = input('num = ')
#     try:
#         num = int(num)
#         if num%2 == 0 :
#             print('true')
#         else:
#             print('false')
#     except Exception:
#         print("格式错误")

'''卖橘子的计算器：写一段代码，提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），最后计算出应该支付的金额！'''
#
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)
# g = foo()
# print(next(g))
# # print("*" * 20)
# print(next(g))

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n = n+1

for n in fib(5):
    print(n)



# if __name__ == '__main__':
#     # print_num
#     count_friut.fib(9)