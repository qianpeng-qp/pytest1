from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# class_name    find_element_by_class_name
driver.find_element_by_class_name("s_ipt").send_keys('携程')
time.sleep(3)
# driver.find_element_by_xpath('//input[contains(@id,\'su\')]').click()
driver.find_element_by_xpath('//*[@id="su"]').click()

# id     find_element_by_id
# driver.find_element_by_id('kw').send_keys('seke')
# -----------------------------------------------------------------------------------------


# name    find_element_by_name
# driver.find_element_by_name('wd').send_keys('sale')
# -----------------------------------------------------------------------------------------


# xpath  find_element_by_xpath 绝对路径
# driver.find_element_by_xpath('/html/body/div/div/div/div[3]/a').click()
# -----------------------------------------------------------------------------------------


# link_text   find_element_by_link_tex 超链接文本
# driver.find_element_by_link_text("新闻").click()
# -----------------------------------------------------------------------------------------


# partial_link_text     find_element_by_partial_link_text
# driver.find_element_by_partial_link_text("新").click()
# -----------------------------------------------------------------------------------------


# xpath  find_element_by_xpath 相对路径
# 1、标签名+节点属性    [//a[@class= "s_bri"]]
# driver.find_element_by_xpath('//input[@name= "wd"]').send_keys('xxx')
# driver.find_element_by_xpath('//a[@name="tj_trhao123"]').click()
time.sleep(2)
driver.find_element_by_xpath(
    '//div[@class="ec-pl-padding-bottom-middle ec-pc_small_head-item ec-block-pc_small_head-0"]//a').click()

# 2、部署属性值匹配//标签名[contains(@属性名，部分属性值)]
# driver.find_element_by_xpath('//a[contains(@name,\'rvide\')]').click()


# 3、使用文本匹配 //标签名[contains(@属性名，部分属性值)]
# driver.find_element_by_xpath('//a[contains(text(),\'贴吧\')]').click()

# -----------------------------------------------------------------------------------------


# css
time.sleep(4)
# driver.find_element_by_css_selector('form[id=\'chinaHotelForm\'] input.w01.inputSel').click()
# driver.find_element_by_xpath('//form[@id=\'chinaHotelForm\']//input[@name=\'cityId\']').send_keys(2)
driver.find_element_by_css_selector('form[id=\'chinaHotelForm\'] input[name=\'cityId\']').send_keys('上海')

