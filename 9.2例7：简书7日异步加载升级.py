from lxml import etree
import requests
import xlwt
import re
import json
from multiprocessing import Pool
context=[]
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

def get_url(url):
    html = requests.get(url,headers=header)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        article_url_part = info.xpath('div/a/@href')[0]
        get_info(article_url_part)

def get_info(url):
    article_url = 'http://www.jianshu.com/' + url
    html = requests.get(article_url,headers=header)
    selector = etree.HTML(html.text)
    author = selector.xpath('//span[@class="name"]/a/text()')[0]
    article = selector.xpath('//h1[@class="title"]/text()')[0]
    date = selector.xpath('//span[@class="publish-time"]/text()')[0]
    word = selector.xpath('//span[@class="wordage"]/text()')[0]
    view = re.findall('"views_count":(.*?),',html.text,re.S)[0]
    comment = re.findall('"comments_count":(.*?),',html.text,re.S)[0]
    like = re.findall('"likes_count":(.*?),',html.text,re.S)[0]
    id = re.findall('{"id":(.*?),',html.text,re.S)[0]    #此信息是异步加载，但是在源代码中的script里面有，用re获取即可
    
    gain=''
    try:
        gain_url = 'http://www.jianshu.com/notes/{}/rewards?count=20'.format(id)
#从Network里看到返回的是一个字符串，即XML/JS类型的，所以要用json.loads转成字典！！！！
        wb_data = requests.get(gain_url,headers=header)
        json_data = json.loads(wb_data.text)
        gain = json_data['rewards_count']
    except IndexError:
        pass

    include_list = []
    try:
        include_urls = ['http://www.jianshu.com/notes/{}/included_collections?page={}'.format(id,i) for i in range(1,10)]
        for include_url in include_urls:
            html = requests.get(include_url,headers=header)
            json_data = json.loads(html.text)
            includes = json_data['collections']
            if len(includes) == 0:
                pass
            else:
                for include in includes:
                    include_title = include['title']
                    include_list.append(include_title)
    except IndexError:
        pass

    info =[author,article,date,word,view,comment,like,gain,include_list]
    context.append(info)

if __name__ == '__main__':
    urls = ['http://www.jianshu.com/trending/weekly?page={}'.format(i) for i in range(1,4)]
    pool = Pool(processes=4)
    pool.map(get_url,urls)

    head=['author','article','date','word','view','comment','like','gain','include_list']
    book=xlwt.Workbook(encoding="utf-8")
    sheet=book.add_sheet('sheet1')
    for i in range(len(head)):
        sheet.write(0,i,head[i])
    i=1
    for each in context:
        for j in range(len(each)):
            sheet.write(i,j,each[j])
        i+=1
    book.save('9.2例7：结果.xls')