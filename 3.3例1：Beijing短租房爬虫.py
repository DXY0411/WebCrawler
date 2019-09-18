import requests
from bs4 import BeautifulSoup
import time   
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}

def get2home(url):
    wb_code=requests.get(url,headers=headers)
    wb_code.encoding='utf8'
    soup=BeautifulSoup(wb_code.text,'lxml')
    address=soup.find('span',attrs={'class':"pr5"}).get_text()
    prise=soup.find('div',attrs={'class':"day_l"}).get_text()
    data1={
            'add':address.strip(),
            'pri':prise.strip()
    }
    print(data1)

def get2line(url):
    wb_code=requests.get(url,headers=headers)
    wb_code.encoding='utf8'
    soup=BeautifulSoup(wb_code.text,'lxml')
    links=soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname') 
    #返回的是列表，即使只有一个也在列表里
    for link in links:
        href=link.get("detailurl")         #标签中的属性信息要用.get("属性名")得到
        get2home(href)


if __name__=='__main__':
    urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(num) for num in range(1,4)]
    for url in urls:
        get2line(url)
        print('\n')
        time.sleep(3)           #每循环一次让程序停止3秒，防止请求网页过快而导致爬虫失败。
