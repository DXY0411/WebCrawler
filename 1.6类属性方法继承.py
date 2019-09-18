class Student:
    books=['a','b','c']
    __siyou=0             #两个下划线，私有属性
    def __init__(self):   #构造函数，隐式调用
        self.age=19
    def go(self):          #无参数函数
        print('go to school!')
    def time(self,hours):  #有参数函数
        print('you studied {} minutes'.format(hours*60))
joy=Student()       #实例化
print(joy.books)
print(joy.age)
#print(joy.__siyou) #会报错 私有属性不能调用
joy.go()
joy.time(4)

class Student2(object):   
    def __init__(self, name):  #构造函数 则object和name是彼此对应的
        self.name = name
s = Student2('Bob')
s.score = 90
print(s.name)
s.job="程序员"
print(s.job)
#给实例绑定属性的方法是通过实例变量，或者通过self变量

#类的继承
class GirlStudent(Student):     #继承Student类
    def girl(self):
        print("I am a girl")
Luna= GirlStudent()
Luna.go()
Luna.girl()

"""
1. 变量命名总结： 
- 1.单下划线开头变量：protected 
- 2.双下划线开头变量：private 
- 3.双下划线开头，双下划线结尾：系统内置变量 
2. 函数命名总结： 
- 1.私有方法：小写和一个前导下划线 
- 2.特殊方法（魔术方法）：小写和两个前导下划线，两个后置下划线 
- 3.函数参数：小写和下划线，缺省值等号两边无空格 def func(self,user=None):
3. 类名称命名： 
- 类总是使用驼峰格式命名，即所有单词首字母大写其余字母小写。
 """