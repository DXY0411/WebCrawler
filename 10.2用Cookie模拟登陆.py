#cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据。
#互联网购物公司通过追踪用户的cookie信息，来给用户提供相关兴趣的商品。
#同样，因为cookie保存了用户的信息，我们便可通过提交cookie来模拟登录网站了。

#手工输入账号和密码进行登录，会发现Network中会加载许多文件。
#不需要查看登录网页的文件信息，而是直接查看登录后的文件信息，可看到相应的cookie信息。

import requests
from lxml import etree
url = 'https://www.douban.com/'
headers = {
    'Cookie':r'll="108288"; bid=wi1_0DaOE2E; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1542106207%2C%22https%3A%2F%2Fwww.so.com%2Fs%3Fie%3Dutf-8%26src%3Dhao_360so_b%26shb%3D1%26hsid%3D5bfa561a2d7614b7%26q%3D%25E8%25B1%2586%25E7%2593%25A3%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1188377039.1542106208.1542106208.1542106208.1; __utmc=30149280; __utmz=30149280.1542106208.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18726; __yadk_uid=xlB7fjJlokuh7daZs1GnEizrMMYAaMer; ps=y; _ga=GA1.2.1188377039.1542106208; _gid=GA1.2.1447021082.1542108024; __utmt=1; _pk_id.100001.8cb4=3c59f65d8408e8ee.1542106207.1.1542108592.1542106207.; __utmb=30149280.12.10.1542106208; _gat_UA-7019765-1=1; dbcl2="187267177:5duXb+3ieuE"',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
res = requests.get(url,headers=headers)
html = etree.HTML(res.text)
user_id=html.xpath('//li[@class="nav-user-account"]/a/span/text()')[0]
print(user_id)          