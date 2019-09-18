#保存成Excel文件的步骤
#1、导入xlwt库
#2、创建book工作簿
#3、创建sheet工作表
#4、写入
#5、保存save
#！！！和csv不同之处在于，csv可以每次累计往文件中写入，比如a+模式
#！！！但是Excel的写入是坐标的写入例如 sheet.write(0,0,'hello')就是在第一格写入
#！！！所以，一般c可以边找寻数据边写入csv文件，但最好把所有采集的数据存在列表中，再利用循环统一遍历坐标写入Excel表格

import requests
from lxml import etree
import time 
import xlwt

context=[]
headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}

def goto_url(url):
    wb_code=requests.get(url,headers=headers)
    wb_code.encoding='utf-8'
    html=etree.HTML(wb_code.text)
    models=html.xpath('//div[@class="book-mid-info"]')
    for model in models:
        id=model.xpath('h4/a/text()')[0].strip()
        author=model.xpath('p[1]/a[1]/text()')[0].strip()
        lab1=model.xpath('p[1]/a[2]/text()')[0].strip()
        lab2=model.xpath('p[1]/a[3]/text()')[0].strip()
        lab=lab1+'*'+lab2
        words=model.xpath('p[3]/span/span/text()')[0].strip()
        #注意，即使span下面还有许多标签，但span直接取了所有的文字
        info_list=[id,author,lab,words]
        context.append(info_list)

if __name__=='__main__':
    urls=['https://www.qidian.com/all?page={}'.format(num) for num in range(1,4)]
    for url in urls:
        goto_url(url)
        time.sleep(1)
    #！！！！！！！！！！！！！！！！！
    head=['id','author','lab','words']
    book=xlwt.Workbook(encoding="utf-8")
    sheet=book.add_sheet('sheet1')
    for i in range(len(head)):
        sheet.write(0,i,head[i])
    i=1
    for each in context:
        for j in range(len(each)):
            sheet.write(i,j,each[j])
        i+=1
    book.save('5.4例5：结果.xls')
    