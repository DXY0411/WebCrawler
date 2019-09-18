#列表[]
a=[1,'a',5.2] 
print(a)           #[1, 'a', 5.2]
print(a[2])        #5.2
print(a[1:])       #['a', 5.2]
print(a[0:2])      #[1, 'a']

#多重循环 zip
a=[1,2,3,4]
b=['a','b','c','d']
for i,j in zip(a,b):
    print(i,j)

urls=['www.baidu.com/{}/'.format(number) for number in range(1,6)]
for url in urls:
    print(url)

#元组()类似列表，只是内容不能修改
b=(1,2,3,4)
print(b[1:])
#b[1]=5会报错

#字典{'':'','':''}
c={'a':'1','b':'2','c':'3','d':'4'}

#集合{'','',''}无序
a=[1,'a',5.2,1,1]
print(a)
d=set(a)  #格式转换成集合
print(d)
f={1,2,1,3}
print(f)