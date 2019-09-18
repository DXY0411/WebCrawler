from selenium import webdriver
from lxml import etree
import time

driver = webdriver.Chrome()
driver.maximize_window()

def get_info(url,page):
    driver.get(url)
    driver.implicitly_wait(10)
    html = etree.HTML(driver.page_source)          #这三行超重要！！之后找信息就和之前练习的一样
    infos = html.xpath('//div[@class="content"]')

    try:
        for info in infos:
            id = info.xpath('div[1]/div[2]/a/text()')[0]
            textpi=info.xpath('p[1]/text()')
            text=''
            for i in textpi:
                text+=i
            print('@'+id)
            print(text.strip())
            print('-'*20)
    except IndexError:
        pass

    page = page + 1
    if page <= 3:
        NextPage(url,page)
    else:
        pass

def NextPage(url,page):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('next').click()  #点击“下一页”
    time.sleep(4)
    get_info(driver.current_url,page)

if __name__ == '__main__':
    page = 1
    url = 'https://weibo.com/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('W_input').clear()
    driver.find_element_by_class_name('W_input').send_keys('哈利波特')
    driver.find_element_by_xpath('//a[@title="搜索"]').click()
    get_info(driver.current_url,page)