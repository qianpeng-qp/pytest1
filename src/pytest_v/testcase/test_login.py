from selenium import  webdriver
from selenium.webdriver import ActionChains
from singdriver import Singdriver
from user import UserAction
import utils
import os
useraction = UserAction()

driver = Singdriver()

def setup_module():
    '''
    执行案例前的操作
    :return:
    '''
    useraction.user_login()

def teardown_module():
    '''
    执行所有测试用例后的操作
    :return:
    '''
    driver.quit()

def teardown():
    '''
    执行每条测试用例后,截屏
    :return:
    '''
    dirname = utils.get_screen_shot()
    filename = utils.get_png_file_name()
    f = os.path.join(dirname,filename)
    driver.save_screenshot(f+'.png')


def test_login():
    """
    测试登陆
    :return:
    """
    #useraction.user_login()

    # 添加断言
    # 1.登录成功应该跳转到首页
    current_url = driver.current_url
    assert current_url=="http://39.107.96.138:3000/","应该跳转到首页"

    # 2. 用户名应该为testuser1
    username = driver.find_element_by_css_selector('span[class="user_name"]>a[class="dark"]').text
    #print('sssss'+username)
    assert username == "testuser1","登录用户名应该为testuser1"



def test_register():
    '''
    发帖
    :return:
    '''
    #driver = webdriver.Chrome()

    driver.get('http://39.107.96.138:3000/topic/create')

    edit = driver.find_element_by_css_selector('div.CodeMirror-scroll')
    edit.click()
    # 定义多个动作 并执行 注意：一定要在最后调用perform()

    action = ActionChains(driver)
    action.move_to_element(edit).send_keys("helloworld").perform()