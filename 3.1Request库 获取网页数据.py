# -*- coding:utf-8 -*-
import requests 
r = requests.get('https://www.baidu.com/') 
print(type(r))        #<class 'requests.models.Response'>
print(r.status_code)  
print(type(r.text))   #<class 'str'>
print(r.text) 
print(r.cookies) 

import requests 
r = requests.get('http://httpbin.org/get')  #响应的是我方的请求头
print(r.status_code) 
print(r.text) 
r = requests.get('http://httpbin.org/get?name=germey&age=22') 
print(r.status_code) 
print(r.text) 
#也可以写成以下形式，利用参数params
data = { 
     'name': 'germey', 
     'age': 22 
}
r = requests.get('http://httpbin.org/get',params=data) 
print(r.text) 
print(r.json()) #调用 json（）方法，就可以将返回结果是 JSON 格式的字符串转化为字典。
#从返回结果看url被自动设置为了http://httpbin.org/get?name=germey&age=22

#防止反爬虫，要更改请求头中的UA
import requests 
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
r= requests.get('http://httpbin.org/get',headers=headers)
print(r.text)  

#当爬虫下来的为二进制文件的时候，用r.content
import requests 
r= requests.get('https://cn.bing.com/az/hprichbg/rb/LiquidNitrogen_ZH-CN9276021591_1920x1080.jpg')
print(r.text) 
print(r.content)
with open('request扒图片(用二进制).jpg','wb') as f: #用with语句将文件存储在当前文件夹中，open()中包括文件名和打开方式
    f.write(r.content)

import requests 
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
r = requests.get('http://www.jianshu.com',headers=headers) 
print(type(r.status_code), r.status_code) #状态码
#如何查看请求头中的信息
print(type(r.headers), r.headers) 
print(type(r.cookies), r.cookies) 
print(type(r.url), r.url) 
print(type(r.history), r.history)    #请求历史

#POST请求，与GET请求类似
import requests 
data ={
    'name ':'germey', 
    'age':'22'
} 
r = requests.post('http://httpbin.org/post',data=data) 
print(r.text) 


#文件上传
import requests 
files = {
    'file':open('1.5file','rb')
} 
r = requests.post('http://httpbin.org/post', files=files) 
print(r.text)

#获取cookie
import requests 
r = requests.get('https://www.baidu.com') 
print(r.status_code)
print(type(r.cookies),r.cookies) 
for key,value in r.cookies.items():  #用 items（）方法将其转化为元组组成的列表
     print(key + '=' + value)
 


