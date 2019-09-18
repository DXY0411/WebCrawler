#BDP可以制作词云
#Python中的Jieba可以进行分词
#利用TAGUL在线制作词云工具，可以制作词云

import jieba.analyse
path = r'C:\Users\PC\Desktop\python文件夹\4.2例2：结果.txt'
fp = open(path,'r',1,encoding='utf-8')
content = fp.read()
try:
    #jieba.analyse.set_stop_words('H:\最近用（笔记本）\python\中文停用词表.txt')
    tags = jieba.analyse.extract_tags(content, topK=50, withWeight=True)
    for item in tags:
        print(item[0]+'\t'+str(int(item[1]*1000)))   #Jieba词频统计的权重是小数，这里乘以1000
finally:
    fp.close()

#此时成功获得了分词，然后转战TAGUL官网
