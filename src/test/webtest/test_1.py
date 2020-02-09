# div.DiscoveryNews h2>span
# //div[@id="col-discovery"]//h2/span[1]

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

#滚动
driver = webdriver.Chrome()
driver.get('http://news.baidu.com/')
js1 = 'window.scrollTo(0，5000)'
js2 = 'document.querySelector("#footerwrapper > div.bottombar > div > div.bot-left > div.qrcode-container.clearfix > div.img-container > img").scrollIntoView()'

while True:
    try:
        text = driver.find_element_by_css_selector('div.DiscoveryNews h2>span').text
        print(text)
        break
    except NoSuchElementException:
        #driver.find_element_by_xpath('//*[@id="footerwrapper"]/div[1]/div/div[1]/div[2]/div[1]/img').location_once_scrolled_into_view()
        driver.execute_script(js2)
        time.sleep(2)



