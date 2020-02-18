from selenium.webdriver import ActionChains

from singdriver import Singdriver

class UserAction:

    '''
    业务相关操作
    '''

    def __init__(self):
        self.driver = Singdriver()

    def user_login(self):
        self.driver.get('http://39.107.96.138:3000/signin')
        self.driver.find_element_by_css_selector('#name').send_keys("testuser1")
        self.driver.find_element_by_css_selector('#pass').send_keys('123456')
        self.driver.find_element_by_css_selector('input[value="登录"]').click()

    def user_send(self):
        self.user_login()
        self.driver.get('http://39.107.96.138:3000/topic/create')

        edit = self.driver.find_element_by_css_selector('div.CodeMirror-scroll')
        edit.click()
        # 定义多个动作 并执行 注意：一定要在最后调用perform()

        action = ActionChains(self.driver)
        action.move_to_element(edit).send_keys("helloworld").perform()
