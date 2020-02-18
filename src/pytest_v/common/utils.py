import os
import time


def get_screen_shot():
    '''
    项目根目录下不存在screnshoots目录，那就创建一个
    :return: screenshots的绝对路径
    '''
    if os.path.isdir('../screnshoots') is False:
        os.mkdir('../screnshoots')
    return os.path.abspath('../screnshoots')


def get_png_file_name():
    '''
    返回文件名年_月_日_时_分_秒
    :return:
    '''
    return time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())

