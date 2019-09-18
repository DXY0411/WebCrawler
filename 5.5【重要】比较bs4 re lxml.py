import requests
from bs4 import BeautifulSoup
import re
from lxml import etree
import time   #time.time()获取时间

headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}

def bs_scraper(url): 
    wb_code= requests.get(url,headers=headers)
    wb_code.encoding = 'utf-8'                   
    soup=BeautifulSoup(wb_code.text,'lxml')     
    ids=soup.select('a > h2')
    contents=soup.select('div.content > span')
    laughters=soup.select('span.stats-vote > i')
    for id_,content,laughter in zip(ids,contents,laughters):
        info={
            'id':id_.text.strip(),
            'content':content.text.strip(),
            'laughter':laughter.text.strip()
        }
        return info

def re_scraper(url):
    wb_code= requests.get(url,headers=headers)
    wb_code.encoding = 'utf-8'                
    ids=re.findall('<h2>(.*?)</h2>',wb_code.text,re.S)
    contents=re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>',wb_code.text,re.S)
    laughters=re.findall(r'<span class="stats-vote">.*?<i class="number">(\d+)</i>.*?</span>',wb_code.text,re.S)
    for id_,content,laughter in zip(ids,contents,laughters):
        info={
            'id':id_.strip(),
            'content':content.strip(),
            'laughter':laughter.strip()
        }
        return info

def lxml_scraper(url):
    wb_code= requests.get(url,headers=headers)
    wb_code.encoding = 'utf-8'
    html=etree.HTML(wb_code.text)      
    models=html.xpath('//div[starts-with(@class,"article block untagged mb15")]')
    for model in models:
        id_=model.xpath('div[1]/a[2]/h2/text()')[0]
        content=model.xpath('a[1]/div/span/text()')[0]
        laughter=model.xpath('div[2]/span[1]/i/text()')[0]
        info={
            'id':id_.strip(),
            'content':content.strip(),
            'laughter':laughter.strip()
        }
        return info          

if __name__=='__main__':
    urls=['https://www.qiushibaike.com/text/page/{}/'.format(num) for num in range(1,3)]
    for name,scraper in[('BeautifualSoup',bs_scraper),('Re',re_scraper),('Lxml',lxml_scraper)]:
        start=time.time()
        for url in urls:
            scraper(url)
            time.sleep(1) 
        end=time.time()
        print(name,end-start)


#!!!结果！！
#BeautifualSoup 4.008716106414795
#CV 2.8033058643341064
#Lxml 3.661334991455078

#比较
#BeautifualSoup   慢   使用比较简单 (注意find_all/select返回的是tag数组)
#cv               快   使用比较困难 (匹配很容易出错)
#Lxml             快   使用比较简单 (但我觉得有一点点困难hhh) (注意批量获取数据时候先找大循环再找细节，灵活运用starts-with())

#总结
#数据量较少用bs合适；数据量较大用lxml合适。

#用了几天觉得还是lxml最好用啦！！！！！
#而且一般是lxml和re一起配合使用！！无敌！！！！！

#bs4获得的标签中的属性信息要用.get("属性名")得到
#lxml是在xpath中最后用@表示出要找的属性 比如<a @title……>中使用xxxx.xpath('a/@title')