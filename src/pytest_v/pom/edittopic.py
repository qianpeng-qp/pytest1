from user import Singdriver

class EditTopicPage:

    def __init__(self):
        self.driver = Singdriver()

    @property
    def breadcrumb_text(self):
        '''
        :return: 导航栏
        '''
        return self.driver.find_element_by_css_selector('li.active').text

    @property
    def error_message(self):
        return self.driver.find_element_by_css_selector('div.alert.alert-error strong').text

    @property
    def alert_msg_text(self):
        '''
        切换到alert获取文字，并点击确定关闭
        :return:
        '''
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text