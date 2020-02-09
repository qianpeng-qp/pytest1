"""
2 爬取百度贴吧，将抓取到的内容 存放到csv⽂件中
3 最终结果格式如下：
4 data.csv
5 标题,内容
6 回复:听说最近耽美⽂超⽕哦《匠⼼》,孙茂顿时急了

12 """


'''document.querySelector()'''
def price():
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    import time


    driver = webdriver.Chrome()

    driver.get('https://www.baidu.com')
    driver.find_element_by_class_name("s_ipt").send_keys('苏宁')
    driver.find_element_by_xpath('//*[@id="su"]').click()
    time.sleep(5)
    driver.find_element_by_css_selector('div.ec-pl-clean-inner-gap.ec-pc_title').click()
    #driver.maximize_window()
    time.sleep(5)
    #print(driver.current_url)        #查询当前windows页面url
    #print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[-1])
    #driver.switch_to.window(driver.window_handles[0]) #切换到前一个页面
    driver.find_element_by_xpath('//input[@id=\'searchKeywords\']').send_keys('iphone11')
    # driver.find_element_by_css_selector('div.search-keyword-box').click()
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.find_element_by_css_selector('input.search-keyword').send_keys('iphone11')
    driver.find_element_by_css_selector('input.search-btn').click()

    #price=driver.find_element_by_css_selector('span.def-price').text
    prices=driver.find_elements_by_css_selector('span.def-price')
    print(len(prices))

    time.sleep(3)
    # print(f'第一台：{prices[0].text}')
    # print(f'最后一台：{prices[-1].text}')
    lastprice = prices[-1]
    c =lastprice.location_once_scrolled_into_view
    time.sleep(10)
    #ActionChains.
    print(lastprice.text)
    driver.close()

def baidu():
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    driver = webdriver.Chrome()

    driver.get('https://www.baidu.com')
    driver.find_element_by_xpath('//a[@name=\'tj_trtieba\']').click()
    driver.find_element_by_xpath('//input[@name = \'kw1\']').send_keys('孙茂书')
    driver.find_element_by_xpath('//a[@class= \'search_btn j_search_post\']').click()
    time.sleep(3)
    #span.p_title  div.s_post>div.p_content

    alltitles=[]
    def craw1_title():
        alltitles1 = driver.find_elements_by_css_selector('span.p_title')
        for ele in alltitles1:
            #print(ele.text)
            alltitles.append(ele.text)

    contents = []
    def craw1_content():
        contents1 = driver.find_elements_by_css_selector('div.p_content')
        for ele in contents1:
            #print(ele.text)
            contents.append(ele.text)





    while True:
        try:
            craw1_title()
            craw1_content()
            driver.find_element_by_css_selector('a[class=\'next\']').click()
            time.sleep(2)
        except NoSuchElementException:
            print('最后一页')
            driver.quit()
            break
    c={}
    for i in range(len(contents)):
        c[alltitles[i]]=contents[i]

    print(c)


if __name__ == '__main__':
    price()
    #baidu()
