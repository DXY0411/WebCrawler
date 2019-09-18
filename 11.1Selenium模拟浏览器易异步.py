#Selenium是一个用于Web应用程序测试的工具，
#Selenium直接运行在浏览器中，就像真正的用户在操作一样。
#由于这个性质，Selenium也是一个强大的网络数据采集工具，其可以让浏览器自动加载页面
#这样，使用了异步加载技术的网页，也可获取其需要的数据。

#Selenium自己不带浏览器，需要配合第三方浏览器来使用。
#通过help命令查看Selenium的Webdriver功能，查看Webdriver支持的浏览器：
""" from selenium import webdriver
    help(webdriver) """
#PACKAGE CONTENTS
    #android (package)
    #blackberry (package)
    #chrome (package)
    #common (package)
    #edge (package)
    #firefox (package)
    #ie (package)
    #opera (package)
    #phantomjs (package)
    #remote (package)
    #safari (package)
    #support (package)
    #webkitgtk (package)


#!!!driver.get()方法请求过后的网页源代码中有异步加载的信息，这样便可以轻松获取Javascript数据
from selenium import webdriver
import selenium
from lxml import etree
driver = webdriver.PhantomJS()
driver.get('https://www.douban.com/')
driver.implicitly_wait(10)                                   #处理需要时间 隐式等待10秒
driver.find_element_by_id('form_email').clear()              #清除输入框数据 
driver.find_element_by_id('form_email').send_keys('-------------运行代码时要写入--------------') #输入账号
driver.find_element_by_id('form_password').clear()
driver.find_element_by_id('form_password').send_keys('-------------运行代码时要写入--------------')
driver.find_element_by_class_name('bn-submit').click()       #单击登入框
print(driver.page_source)   

#能看出来虽然成功输入了但是没输入验证码，所以没能登陆成功   
