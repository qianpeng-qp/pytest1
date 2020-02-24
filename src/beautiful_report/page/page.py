from selenium import webdriver

class Page:
    '''
    基础页面类
    '''

    login_url = 'http://39.107.96.138:3000'

    def __init__(self, seleium_driver, base_url=login_url):
        self.driver = seleium_driver
        self.base_url = base_url
        # 设置超时时间30秒
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def get_url(self):
        return self.base_url + self.url
