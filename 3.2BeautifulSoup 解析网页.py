#通过BeautifulSoup将网页源代码解析为soup文档
#此文档按照标准缩进格式的结构输出
#BS的解析库：python标准库/lxml解析库/xml解析库/html5lib解析库 
#推荐'lxml'

#标准缩进代码
import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
res= requests.get('http://www.baidu.com',headers=headers)  #请求网页
res.encoding = 'utf8'                     #！！！！都加这么一句就可以避免网站不是utf8而导致的中文调试乱码
soup=BeautifulSoup(res.text,'lxml')       #解析网页
print(type(soup))                         #BeautifulSoup对象
[s.extract() for s in soup('script')]     #去除所有的script
[s.extract() for s in soup('style')]      #去除所有的style
print(type(soup.prettify())) 
print(soup.prettify())                    #标准缩进格式
print(soup)                               #没有缩进格式

#select()语法    返回的内容是列表[] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1、通过标签名查找 .select('div')
#2、通过类名查找   .select('.name')  （此时 class=‘name’）
#3、通过id名查找   .select('#name')   (此时 id=‘name’)
#4、通过子标签查找 .select('div>a')
#5、通过属性查找   .select('a[href="http:xxx"]')   (此时<a href="xxx" )
#6、混合查找       .select(div.name>a[href="http:xxx"])

#查询输出相应的tag及其文本
import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
res= requests.get('http://www.xiaozhu.com/',headers=headers)   #请求网页
res.encoding = 'utf8'                                          #每次都加一句！！！
soup=BeautifulSoup(res.text,'lxml')                            #解析网页
print(soup.find('div',attrs={'class':'index_T'}))              #返回文档中符合条件的第一个Tag  
print(type(soup.find('div',attrs={'class':'index_T'})))
#soup.find('div',_class='index_T')                             同理
#soup.find('div','index_T')                                    同理        
print(soup.find_all('div',attrs={'class':'index_T'}))          #返回文档中符合条件的所有Tag  是一个列表[]

#用当前审查元素右键copy selector，再用select函数
print(soup.select('#load_Ajax_IndexRecommend > div.index_T'))       #等价于find
print(type(soup.select('#load_Ajax_IndexRecommend > div.index_T')))
print(type(soup.select('#load_Ajax_IndexRecommend > div.index_T')[0]))
""" print(soup.select('body > div:nth-of-type(1) > div:nth-of-type(10)'))  #等价于find
删除此时谓语部分相当于等价成find_all()
print(soup.select('body > div > div:nth-of-type(10)'))  #等价于find_all """

print(soup.find('div',attrs={'class':'index_T'}).get_text())    #用get_text()函数搭配这三个查找选取的操作函数，显示文本                        
print(soup.find('div',attrs={'class':'index_T'}).get("class"))  #！！！标签中的属性信息要用.get("属性名")得到

#注意之前请求网页之后的是.text属性，输出文本  ，是requests库里的text属性
#现在的是.get_text()函数  也可以是.text属性  ，是bs4库里的.get_text()方法、text属性。
#！！！标签中的属性信息要用.get("属性名")得到
