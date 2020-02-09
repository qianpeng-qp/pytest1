from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.find_element_by_class_name("s_ipt").send_keys('苏宁')
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)
driver.find_element_by_css_selector('div.ec-pl-clean-inner-gap.ec-pc_title').click()
# driver.maximize_window()
time.sleep(5)
# print(driver.current_url)        #查询当前windows页面url
# print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])
#driver.switch_to.window(driver.window_handles[0])  # 切换到前一个页面
driver.find_element_by_xpath('//input[@id=\'searchKeywords\']').send_keys('iphone11')
# driver.find_element_by_css_selector('div.search-keyword-box').click()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.find_element_by_css_selector('input.search-keyword').send_keys('iphone11')
driver.find_element_by_css_selector('input.search-btn').click()

#price=driver.find_element_by_css_selector('span.def-price').text
prices = driver.find_elements_by_css_selector('span.def-price')
driver.execute_script("window.scrollBy(0,4000)")

print(len(prices))

time.sleep(3)
# print(f'第一台：{prices[0].text}')
# print(f'最后一台：{prices[-1].text}')
lastprice = prices[-1]
c = lastprice.location_once_scrolled_into_view
time.sleep(10)
# ActionChains.
print(lastprice.text)