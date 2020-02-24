from page import Page
from selenium.webdriver.common.by import By


class topic_page(Page):
    '''
    发帖页面
    '''

    url = '/api/v1/topics'

    # 定位器
    # username = (By.CSS_SELECTOR, '#name')
    # password = (By.CSS_SELECTOR, '#pass')
    # submit_loc = (By.CSS_SELECTOR, 'input[value="登录"]')