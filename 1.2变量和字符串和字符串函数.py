#普通输出、加和输出、乘法输出
a=4
b=5
print(a,b)
c='a1'
print(a+b)
#print(a+c)
print(c*3)

#字符串切片和索引
d='I Love You'
print(d[0])      #I
print(d[0:5])    #I Lov
print(d[-1])     #u
print(d[-3:-1])  #Yo

#字符串方法
#①split（）分割后存到列表
e='www.baidu.com'
print(e.split('.')) #若没提供分隔符，则程序把所有的空格都看作分隔符，空格制表换行
#②replace（）查找和替换
print(e.replace('www','WWW'))
#③strip()去除两侧空格/指定字符串
f='   I am Joy    '
print(f.strip())         #I am Joy
f='*****I am Joy!!!!!'
print(f.strip('*'))      #I am Joy!!!!!
f='*****I am Joy!!!!!'
print(f.strip('*!'))     #I am Joy


#format()减少代码使用量
content=input("请输入内容：")
url_path='www.baidu.com/{}/'.format(content)
print(url_path)
