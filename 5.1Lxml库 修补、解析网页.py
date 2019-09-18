from lxml import etree
text='''
<a target="_blank">
   <h2>1234
</a>
'''
html=etree.HTML(text)
print(type(html))
print(html)    #是Element对象
result=etree.tostring(html)
print(result)  #发现补全了</h2>,并且添加了html和body标签

#用Lxml库解析网页
import requests
from lxml import etree
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
res= requests.get('http://www.baidu.com',headers=headers)  #请求网页
res.encoding = 'utf8'                     #！！！！都加这么一句就可以避免网站不是utf8而导致的中文调试乱码
html=etree.HTML(res.text)
print(etree.tostring(html))

