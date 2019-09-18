from selenium import webdriver
import time
import csv

driver = webdriver.PhantomJS()
driver.maximize_window()                                #窗口最大化

def get_info(qq):
    driver.get('http://user.qzone.qq.com/{}'.format(qq))
    driver.implicitly_wait(10)

    try:
        driver.find_element_by_id('login_div')           #登录页面
    except:
        a = False
    if a == True:
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！在iframe中的信息，要用switch_to.frame()
        driver.switch_to.frame('login_frame')            
        driver.find_element_by_id('switcher_plogin').click()#选择用账号密码登录
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('-------------运行代码时要写入--------------')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('-------------运行代码时要写入--------------')
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    
    try:
        driver.find_element_by_id('QM_Feeds_Container')
        b = True
    except:
        b = False
    if b == True:
        driver.switch_to.frame('QM_Feeds_Iframe')
        contents = driver.find_elements_by_xpath('//div[@class="f-info"]')
        times = driver.find_elements_by_xpath('//span[@class=" ui-mr8 state"]')
        for content, tim in zip(contents, times):
            data = {
                'time': tim.text,
                'content': content.text
            }
            print(data)

if __name__ == '__main__':
    """ qq_lists = []
    fp = open('C:/Users/LP/Desktop/QQmail.csv')
    reader = csv.DictReader(fp)
    for row in reader:
        qq_lists.append(row['电子邮件'].split('@')[0])
    fp.close() 
    for item in qq_lists:
        get_info(item)"""
    get_info('1448983098')