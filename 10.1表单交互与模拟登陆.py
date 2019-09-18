#POST表单交互
#Requests库的POST方法使用简单，只需要简单地传递一个字典结构的数据给data参数。
#这样，在发起请求时会自动编码为表单形式，以此来完成表单的填写。

#观察豆瓣网页的登录区域
#一般表单都是<form>表单中的内容
#对于表单源代码，有几个重要组成部分。分别是form标签的action属性和input标签。
#Action属性为表单提交的URL。而input为表单提交的字段，input标签的name属性就是提交表单的字段名称。

import requests
from lxml import etree
url = 'https://www.douban.com/accounts/login'      #form标签的action属性中得知
params = {
    'source':'index_nav',
    'form_email':'kabb1999@sina.com',
    'form_password':'DxyJason19990411'
}                                 
res = requests.post(url,data=params)
html = etree.HTML(res.text)
user_id=html.xpath('//li[@class="nav-user-account"]/a/span/text()')[0]
print(user_id)                      #打印出账号用户名则说明登陆成功

#手动登录的话，看Network会发现有一个login文件
#可以看到地址url和Form Data的信息
#与上方我们自己填入的相一致·

