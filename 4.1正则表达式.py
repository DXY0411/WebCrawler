#一般字符： .  \  [...]
#预定义字符集：  \d \D \s \S \w \W
#数量词： * + ？ {m} {m,n}
#边界匹配： ^ $ \A \Z
#(.*?)表示匹配任意的字符

import re
a='abc123\t\\n'
print(a)           #  abc123  \n
 
#search()函数 匹配第一个符合正则表达式的内容并返回
num= re.search(r'\d+',a)       
print(type(num))   #<class 're.Match'>
print(num)         #返回的是正则表达式对象 
print(num.group()) #用group()函数获取match的信息 <re.Match object; span=(3, 6), match='123'>

#sub()函数替换匹配项   类似于字符串函数replace()
t=re.sub(r'\D','*',a)
print(t)

#！！！findall()函数 匹配所有符合条件的内容，并以列表返回。
#！！！爬虫实战中，最常用(.*?)表示匹配任意的字符并且作为返回值返回
b='xxxjrgrntxxxddddxxx33xxx888'
t=re.findall('xxx(.*?)xxx',b)
m=re.findall(r'xxx(\d+)xxx',b)
print(t)                                        #['jrgrnt', '33'] 
print(m)                                        #['33']

#例子：
import re
import requests
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
res=requests.get('http://bj.xiaozhu.com/',headers=headers)
prices=re.findall('<span class="result_price">&#165;<i>(.*?)</i></span>',res.text)
for i in prices:
    print(i)

#re模块修饰符 最常用的是re.S:使匹配包括换行在内的所有字符
#例如
import re
a='''xxx123
xxx'''
b=re.findall('xxx(.*?)xxx',a)
c=re.findall('xxx(.*?)xxx',a,re.S)
print(b)   #[] 
print(c)   #['123\n']      这是因为findall是逐行匹配的，当第一行没有匹配到数据的时候，从第二行开始重新匹配
print(c[0].strip())  #123




#所以现在匹配信息并返回有了以下几种方法：
#1、request库的get  （text）
#2、bs4库的BeautifulSoup/find/find_all/select  （get_text()）
#3、re库的search/findall    （返回的是列表）