f = open('1.5file','w')       #覆盖原数据写入用w
f.write('hello world')
f.close()

f = open('1.5file','r')
content=f.read()
print(content)
lines=f.readlines()
print(lines)                  #列表内容为每一行的内容
f.close()
#此时f.read()已经读完，指针指向最后，再f.readlines()将不会再读出数据

f = open('1.5file','a')       #追加写入用a
f.write('追加文本')
f.close()

#！！！！！！！！！！！！！！！！！！！！！！！！！！！！
#open(file, mode, buffering, encoding, errors, newline, closefd, opener)
#其中file是文件名，mode是打开模式，
#buffering 当文件是二进制为0，是文本用1.
#encoding='utf-8' 通常和requests.get之后res.encoding='utf-8'配合使用
#with open('结果.txt','a+',1,encoding='utf-8') as f:
#带 加号+ 的模式就是同时应用与读和写