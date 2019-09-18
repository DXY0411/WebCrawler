#函数
def change_num(number):
    hid_num=number.replace(number[3:7],'*'*4)
    print(hid_num)
change_num('12345678907')

#判断语句和while循环
def count():
    i=0
    while i<3:
         password=input("请输入序号：")   #input返回的是string类型
         if password=='1':
            print('hello Dxy')
         elif password=='2':
            print('hello Cjx')
         else:
            print('go away!')
         i+=1
count()

#for循环
#for i in 集合
for i in range(10):   #输出0,1…… 9
    print(i)
for i in range(2,10): #输出2，3…… 9
    print(i)
for i in range(1,10,2):  #从1到9每隔2个输出
    print(i)             #1 3 5 7 9
for i in [1,2,3,4]:
    print(i)