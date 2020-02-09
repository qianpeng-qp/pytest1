from selenium import webdriver
from selenium.webdriver.common.action_chains  import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()


def delete():
    driver.get("http://39.107.96.138:3000/signin")

    driver.find_element_by_id('name').send_keys("testuser1")
    driver.find_element_by_id('pass').send_keys('123456')

    driver.find_element_by_css_selector('input[value="登录"]').click()
    # 进入个人中心
    driver.find_element_by_css_selector('span[class="user_name"]>a.dark').click()
    # 点击最近创建的第一个话题
    driver.find_element_by_css_selector('div.cell a[class="topic_title"]').click()
    # 点击删除按钮
    driver.find_element_by_css_selector('i[title="删除"]').click()

    # 切换alert
    alert = driver.switch_to.alert
    # 获取文本
    alert_text = alert.text
    print(alert_text)
    # 点击确定
    alert.accept()

    # 点击取消
    # alert.dismiss()



'''加帖子'''
driver = webdriver.Chrome()

driver.get("http://39.107.96.138:3000/signin")


driver.find_element_by_id('name').send_keys("testuser1")
driver.find_element_by_id('pass').send_keys('123456')

driver.find_element_by_css_selector('input[value="登录"]').click()

driver.get('http://39.107.96.138:3000/topic/create')


edit = driver.find_element_by_css_selector('div.CodeMirror-scroll')
edit.click()
# 定义多个动作 并执行 注意：一定要在最后调用perform()
action = ActionChains(driver)
action.move_to_element(edit).send_keys("helloworld").perform()
# 模拟ctrl a
action.key_down(Keys.CONTROL)
action.send_keys('a')
action.key_up(Keys.CONTROL)
# 模拟ctrl b
action.key_down(Keys.CONTROL)
action.send_keys('b')
action.key_up(Keys.CONTROL)

action.perform()


# driver.find_element_by_css_selector('[id="tab-value"]').click()
# driver.find_element_by_css_selector('option[value="job"]').click()

# 使用Select 类定位元素
# Select(driver.find_element_by_css_selector('select[id="tab-value"]')).select_by_index(1)
# 通过value值
# Select(driver.find_element_by_css_selector('select[id="tab-value"]')).select_by_value("ask")
# 通过可见文本值来操作



Select(driver.find_element_by_css_selector('select[id="tab-value"]')).select_by_visible_text("问答")

driver.find_element_by_id('title').send_keys("123131231231231231")

driver.find_element_by_css_selector('input[value="提交"]').click()
