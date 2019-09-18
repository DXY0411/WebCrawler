#节点选择：
#nodename / // . .. @
#Xpath在元素信息右键“Copy Xpath”即可获得

#获取单一信息例子
import requests
from lxml import etree
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
wb_code=requests.get('https://www.qiushibaike.com/text/',headers=headers)
wb_code.encoding='utf-8'
html=etree.HTML(wb_code.text)
#找了一个人的id，右键获取Xpath，是‘//*[@id="qiushi_tag_121194996"]/div[1]/a[2]/h2’
#在后面加上text()函数可以获取标签中的文字信息
#.xpath()返回的是列表类型 
id=html.xpath('//*[@id="qiushi_tag_121184998"]/div[1]/a[2]/h2/text()')[0]
print(id.strip())


#获取批量信息的例子
#此时不能像bs4的select()函数那样去除谓语，要先找循环点，再在循环中找目标
#观察大框架，发现每个笑话模块中，都以‘<div class="article block untagged mb15 …………"…………>开头
import requests
from lxml import etree
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
wb_code=requests.get('https://www.qiushibaike.com/text/',headers=headers)
wb_code.encoding='utf-8'
html=etree.HTML(wb_code.text)
#tag[starts-with(@属性名，“包含字符串”)]    表示拥有“包含特定字符的属性”的tag
models=html.xpath('//div[starts-with(@class,"article block untagged mb15")]')
for model in models:
    id=model.xpath('div[1]/a[2]/h2/text()')[0]
    print(id.strip())
