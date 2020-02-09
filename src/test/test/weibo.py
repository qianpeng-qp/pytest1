from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://weibo.com/')

time.sleep(15)
driver.implicitly_wait(100)
#driver.find_element_by_css_selector('input[id="loginname"]').send_keys('111111')
ele= WebDriverWait(driver,25,0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[id="loginname"]')))
ele.send_keys('12345')
driver.find_element_by_css_selector('div.info_list.password input[name="password"]').send_keys('111111')