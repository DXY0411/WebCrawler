# 异步加载技术（AJAX）
# 在不重新加载整个网页的情况下，对网页的某部分进行更新
# 由该段代码是否在页面源代码中来判断是否为异步加载信息
# 需要用到逆向工程，即了解网页是如何加载这些数据的
# 需要用到浏览器的Network选项卡。
# 用逆向工程的思想爬虫，通常被称为“抓包”
import requests
from lxml import etree
import xlwt
headers={
    'User-Agent':'Chrome/51.0.2704.63 Safari/537.36'
}
context=[]

def get_time_info(url,page):        #从首页进入的时候是第一页的动态，从第二页动态开始的地址有规律可循
    user_id = url.split('/')        #所以进来先找到第一页要用的信息，然后进入下一个页面
    user_id = user_id[4]
    if url.find('page='):
        page = page+1
    res = requests.get(url,headers=headers)
    html = etree.HTML(res.text)
    infos = html.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        dd = info.xpath('div/div/div/span/@data-datetime')[0]
        type = info.xpath('div/div/div/span/@data-type')[0]
        context.append([dd,type])

    id_infos = html.xpath('//ul[@class="note-list"]/li/@id')
    if page<4:                     #本实验中只找了前三页的信息内容
        feed_id = id_infos[-1]
        max_id = feed_id.split('-')[1]
        max_id=str(int(max_id)-1)
        #print(max_id)
        next_url = 'http://www.jianshu.com/users/%s/timeline?max_id=%s&page=%s' % (user_id, max_id, page)
        get_time_info(next_url, page)    
#从27行到这里都是找寻下一次动态加载的地址，这是由逆向工程分析出来的方法所得。

if __name__ == '__main__':
    get_time_info('http://www.jianshu.com/users/9104ebf5e177/timeline',1)
    head=['time','type']
    book=xlwt.Workbook(encoding="utf-8")
    sheet=book.add_sheet('sheet1')
    for i in range(len(head)):
        sheet.write(0,i,head[i])
    i=1
    for each in context:
        for j in range(len(each)):
            sheet.write(i,j,each[j])
        i+=1
    book.save('9.1例6：结果.xls')