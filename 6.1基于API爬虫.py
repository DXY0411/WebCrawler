#基于API的爬虫的一般步骤 （APISTORE网站里有很多付费api）（聚合数据网站）
#1、在网站注册开发者账户用户名，获得相应的开发者密钥 （需要密钥是因为 ①收费 ②限制调用次数）
#2、在网站的API帮助说明文档中找到自己需要使用的API,确认API请求的限制次数,确认调用API需要使用的参数
#3、在联网状态下，编写正确代码调用API
#4、从API返回的内容（JSON格式）获取正确的属性
#5、将获取的内容存储到本地（文件或数据库）
#相当于爬虫的代码已经被写好了
#所以我们在爬虫前，先考虑该网站是否有API，如果有的话，调用API即可，如果没有再自己写爬虫代码

#调用API的过程也使用request请求。GET/POST/PUT/DELETE……

#这个例子是百度地图的api
import requests
import json
import pprint
address=input('请输入地点：')
par={'address':address,'key':'cb649a25c1f81c1451adbeca73623251'} #此处用的示例中的kay，参数形式从说明文档得知
url='http://restapi.amap.com/v3/geocode/geo'
res=requests.get(url,params=par)
print(type(res.text))              #返回的是json字符串，是str类型
print(res.text)
json_data=json.loads(res.text)     #json.loads()函数 把json字符串转化成dict字典！！！！！！！
print(type(json_data))             #返回的是dict类型
print(json_data)
""" #import pprint
pprint.pprint(json_data)           #pprint能结构化打印数据！！！！！！！！！！！！！！！！！！

#得到返回信息然后进行观察之后，就能直接提取自己想要的信息了 比如提取经纬度
t=json_data['geocodes'][0]['location']
print(t)
 """

