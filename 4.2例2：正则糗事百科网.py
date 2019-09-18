import requests
import re
import time   

headers={
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
}
result=[]

def get2line(url):
    wb_code=requests.get(url,headers=headers)
    wb_code.encoding='utf8'
    contents=re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>',wb_code.text,re.S)
    #！！！！这里注意因为查看源代码时发现<div class="content">和<span>之间有好多空格和空行，
    #所以要用.*?进行前后两次的匹配
    #否则不能读取contents成功
    names=re.findall('<h2>(.*?)</h2>',wb_code.text,re.S)
    for name,content in zip(names,contents):
        info={
            'name':name.strip(),
            'content':content.strip()
        }
        result.append(info)

if __name__=='__main__':
    urls=['https://www.qiushibaike.com/text/page/{}/'.format(num) for num in range(1,3)]
    for url in urls:
        get2line(url)
        time.sleep(3) 
    with open('4.2例2：结果.txt','a+',1,encoding='utf-8') as f:
        for each in result:
            f.write(each['name']+'\n')
            f.write(each['content']+'\n\n')

                