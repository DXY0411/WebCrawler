#存入csv文件的流程
#1、打开文件fp=open('xxx.csv','a+',1,encoding='utf-8')
#2、设置文件writer：writer=csv.writer(fp)
#3、用writer.writerow()写入 写入的通常是列表
#4、都写完之后在末尾关闭文件 fp.close()
import requests
from lxml import etree
import time 
import csv

headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}

#！！！csv文件的打开和写入 
# 打开文件之后需要声明一个作者！！！ 
# （在代码最后要关闭文件 fp.close()）
fp=open('5.3例3：结果.csv','a+',1,encoding='utf-8')
writer=csv.writer(fp)   
writer.writerow(('id','main_author','publish_time','price'))

def get_into(url):
    wb_code = requests.get(url,headers=headers)
    wb_code.encoding='utf-8'
    html=etree.HTML(wb_code.text)
    models=html.xpath('//tr[@class="item"]')
    for model in models:
        id=model.xpath('td[2]/div[1]/a/@title')[0].strip()   #注意用了@title读取属性内容！！！！！
        detail=model.xpath('td[2]/p[1]/text()')[0].split('/')
        main_author=detail[0].strip()
        publish_time=detail[-2].strip()
        price=detail[-1].strip()
        writer.writerow((id,main_author,publish_time,price))
    
if __name__=='__main__':
    urls=['https://book.douban.com/top250?start={}'.format(num) for num in range(0,75,25)]
    for url in urls:
        get_into(url)
        time.sleep(1)
    fp.close()

#！！！！！！！！！！
#发现双击这个生成的csv文件之后，打开发现乱码 
#解决方法：通过记事本打开，将其另存为编码为UTF-8的文件
    