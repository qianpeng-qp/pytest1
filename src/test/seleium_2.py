from aip import AipOcr
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

client = AipOcr('18237057','U7Z6NnsQNOLkdTWITItGgf1w','9cRLl0ZMWQCEkFxQeb73zC4feFsCry4e')

driver = webdriver.Chrome()
driver.get('http://47.100.225.199/index.php?s=/index/user/logininfo.html')

driver.find_element_by_name('accounts').send_keys('helloworld')
driver.find_element_by_name('pwd').send_keys('123456')


#返回验证码
def get_verifycode(filePath):
    verycode = ''
    with open(filePath, 'rb') as fp:
        ret = fp.read()             #返回文件流
        res= client.basicGeneral(ret)  #识别后的结果
        for i in res['words_result']:
            word=i['words'].replace(' ','')
            verycode+=word
    return verycode


while True:
    try:
        img = driver.find_element_by_id('form-verify-img')
        img.screenshot('./img1.png')
        t = get_verifycode('img1.png')
        verify_input = driver.find_element_by_name('verify')
        verify_input.clear()
        verify_input.send_keys(t)
        time.sleep(1)
        driver.find_element_by_css_selector('div.am-form-group.am-form-group-refreshing>button[type=\'submit\']').click()

        img.click() #更换图片
        time.sleep(1)
        ActionChains(driver).move_by_offset(0, 0).perform()
        time.sleep(1)
    except NoSuchElementException:
        break
print('succes')






