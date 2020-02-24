from selenium import webdriver

class Singdriver:
    '''
        单例模式，统一管理浏览器的实例
    '''

    __instance = None

    def __new__(cls, *args, **kwargs):
        '''new 创建对象时调用,单例模式统一管理浏览器实例'''
        if cls.__instance is None:
            cls.__instance = webdriver.Chrome()
        cls.__instance.implicitly_wait(10)
        cls.__instance.maximize_window()
        return cls.__instance

# if __name__ == '__main__':
#     dir1 = Singdriver()
#     dir2 = Singdriver()
#     print(dir2)
#     print(dir2)