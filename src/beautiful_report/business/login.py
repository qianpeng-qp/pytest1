from login_page import LoginPage
from singdriver import Singdriver


class user:
    '''
    注册登陆
    '''

    def login(self):
        loginpage = LoginPage(Singdriver())
        loginpage.open()


if __name__ == '__main__':
    user = user()
    user.login()
