from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def yuansu():
    driver = webdriver.Chrome()
    driver.get('https://search.suning.com/iPhone%2011/')
    eles = driver.find_elements_by_css_selector('span.def-price')
    for i in eles:
        # 获取元素属性值
        sku = i.get_attribute('datasku')
        band_id = i.get_attribute('brand_id')
        color = i.value_of_css_property('color')  #获取颜色
        print(sku,band_id)

    driver.get('https://www.baidu.com')
    name = driver.find_element_by_css_selector('#kw').get_property('name')  #仅能获取name
    driver.find_element_by_class_name("s_ipt").send_keys('苏宁')
    driver.find_element_by_class_name("s_ipt").submit() #enter键
    print(name)


def iframe():
    driver = webdriver.Chrome()
    driver.get('https://login.anjuke.com/login/form')
    iframe = driver.find_element_by_id('iframeLoginIfm')
    driver.switch_to.frame(iframe)# 切换到iframe里
    driver.find_element_by_id('phoneIpt').send_keys('13020207396')
    driver.find_element_by_id('smsIpt').send_keys('123311')
    driver.switch_to.parent_frame()  #返回上一层
    driver.find_element_by_xpath('//a[contains(text(),\'关于安居客\')]').click()

def roll():
    driver = webdriver.Chrome()
    driver.get('https://account.aliyun.com/register/register.htm')
    ifram = driver.find_element_by_id('alibaba-register-box')
    driver.switch_to.frame(ifram)
    slides = driver.find_element_by_css_selector('div[id="nc_1__scale_text"]')
    slides.location_once_scrolled_into_view  #确认x，y完整
    print(slides.location)

    width = slides.value_of_css_property('width')
    width = int(width.split('px')[0])  #长度
    drag = driver.find_element_by_css_selector('span[id="nc_1_n1z"]')
    print("width:",width)
    # 在元素上按下鼠标左键，移动鼠标，释放鼠标，执行。
    ActionChains(driver).move_to_element(drag).click_and_hold().move_by_offset(width,0).release().perform()


def window():
    driver = webdriver.Chrome()
    # 最大化窗口
    driver.maximize_window()
    # 最小化
    driver.minimize_window()
    # 全屏
    driver.fullscreen_window()

    driver.get("https://www.baidu.com")
    driver.find_element_by_css_selector('#kw').send_keys("helloworld")
    driver.find_element_by_css_selector('#kw').submit()

    # 后退
    driver.back()
    # 前进
    driver.forward()
    # 刷新
    driver.refresh()

    # 退出
    driver.quit()

from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import  time
driver = webdriver.Chrome()
driver.maximize_window()
# 设置页面加载时间
driver.set_page_load_timeout(30)
# 全局等待某个元素显示出来
driver.implicitly_wait(20)
driver.get('https://www.juhe.cn/?')
start_time = time.perf_counter()
iframe1 = driver.find_element_by_css_selector('iframe[id="layui-layer-iframe1"]')
driver.switch_to.frame(iframe1)
try:

    # ele = driver.find_element_by_css_selector('div.inputWrap > [id="mobilephone"]')
    #EC.筛选出xx BY是获取元素
    ele= WebDriverWait(driver,15,0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.inputWrap > [id="mobilephone"]')))
    ele.send_keys('12345')
except NoSuchElementException as e:
    print(driver.page_source)
    print(e)
finally:
    driver.find_element_by_css_selector('div.inputWrap > [id="mobilephone"]').send_keys('11111')

    pass
end_time = time.perf_counter()
print(f"查找元素一共使用 时间： {end_time-start_time}")

# ele = WebDriverWait(driver,6,0.3).until(lambda x:x.find_element_by_css_selector('div.inputWrap > [id="mobilephone"]'))

# ele.send_keys('1234')