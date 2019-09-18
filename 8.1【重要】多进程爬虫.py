# 当计算机运行程序时，就会创建包含有代码和状态的进程。
# 这些进程会通过计算机的一个或多个CPU执行。
# 不过，同一时刻每个CPU只会执行一个进程，
# 然后在不同进程间快速切换，这样就给人以多个程序同时运行的感觉。
# 同理，在一个进程中，程序的执行也是在不同线程间进行切换的，每个线程执行程序的不同部分。

#!!!!!!!!!!在要爬取的数据很多的时候，多进程爬虫有用
#!!!!!!!!!!不一定进程越多速度越快
#!!!!!!!!!!在程序运行时可以看资源管理器，有好几个python在运行

#多进程语法：
#from multiprocessing import Pool    导入库
#pool =Pool(processes=3)             创建进程池并且设置进程数
#pool.map(func,iterable)             func是爬虫函数，iterable是迭代参数，通常是要进行爬虫的urls的迭代
#具体见以下例子

import requests
import re
import time
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def re_scraper(url):
    res = requests.get(url,headers=headers)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughs = re.findall(r'<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
    comments = re.findall(r'<i class="number">(\d+)</i> 评论',res.text,re.S)
    for id,content,laugh,comment in zip(ids,contents,laughs,comments):
        info = {
            'id':id,
            'content':content,
            'laugh':laugh,
            'comment':comment
        }
        return info

if __name__ == '__main__':
    urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,6)]

    start_1 = time.time()
    for url in urls:
        re_scraper(url)
    end_1 = time.time()
    print('串行爬虫',end_1-start_1)

    start_2 = time.time()
    pool = Pool(processes=2)
    pool.map(re_scraper, urls)
    end_2 =time.time()
    print('两个进程',end_2-start_2)

    start_3 = time.time()
    pool = Pool(processes=4)
    pool.map(re_scraper, urls)
    end_3 =time.time()
    print('四个进程',end_3-start_3)