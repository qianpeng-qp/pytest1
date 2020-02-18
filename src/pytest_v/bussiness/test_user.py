from selenium import webdriver
from selenium.webdriver import ActionChains
from  singdriver import Singdriver
class test_login:
    '''
    用户登陆
    '''
    def __init__(self):
        self.driver = Singdriver()

    def test_login(self):
        """
        测试登陆
        :return:
        """
        # driver = webdriver.Chrome()
        self.driver.get('http://39.107.96.138:3000/signin')
        self.driver.find_element_by_css_selector('#name').send_keys("testuser1")
        self.driver.find_element_by_css_selector('#pass').send_keys('123456')
        self.driver.find_element_by_css_selector('input[value="登录"]').click()

        # 添加断言
        # 1.登录成功应该跳转到首页
        current_url = self.driver.current_url
        assert current_url == "http://39.107.96.138:3000/", "应该跳转到首页"

        # 2. 用户名应该为testuser1
        username = self.driver.find_element_by_css_selector('span[class="user_name"]>a[class="dark"]').text
        print('sssss'+username)
        #assert username == "testuser1", "登录用户名应该为testuser1"

    def test_sendmail(self):
        '''
        发帖
        :return:
        '''
        self.driver.get("http://39.107.96.138:3000/signin")

        self.driver.find_element_by_id('name').send_keys("testuser1")
        self.driver.find_element_by_id('pass').send_keys('123456')

        self.driver.find_element_by_css_selector('input[value="登录"]').click()

        self.driver.get('http://39.107.96.138:3000/topic/create')

        edit = self.driver.find_element_by_css_selector('div.CodeMirror-scroll')
        edit.click()
        # 定义多个动作 并执行 注意：一定要在最后调用perform()

        action = ActionChains(self.driver)
        action.move_to_element(edit).send_keys("helloworld").perform()