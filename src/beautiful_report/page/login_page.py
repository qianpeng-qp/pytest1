from page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    '''
    登陆页面
    '''

    url = '/signin'

    # 定位器
    username = (By.CSS_SELECTOR, '#name')
    password = (By.CSS_SELECTOR, '#pass')
    submit_loc = (By.CSS_SELECTOR, 'input[value="登录"]')
