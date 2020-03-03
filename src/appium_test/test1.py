from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'                #平台名称
desired_caps['deviceName'] = '192.168.0.105:5555'         #建立连接
#desired_caps['deviceName'] = 'Coolpad 5263S'         #机器名
#desired_caps['udid'] = '2b435cfe'         #真机


# desired_caps['app'] = r'D:\kaoyan3.1.0.apk'
# desired_caps['appPackage'] = 'com.tal.kaoyan'
# desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
#
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# driver.implicitly_wait('10')
# driver.find_element_by_id('android:id/button2').click()
# driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
# driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('122112112')
# driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('111111111')
# time.sleep(10)
# driver.find_element_by_id('com.tal.kaoyan:id/login_scan_btn').click()
driver.find_element_by_id('com.ss.android.ugc.aweme:id/a_8').click()

