#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
print('---------------获取对象信息-----------------')
#判断对象类型 type,<class 'int'>
print(type(123))
print(type('hello'))
#判断函数
print(type(abs))
#判断类型是否相同
if(type(123) == type(456)):
	print('相同类型')
#isinstance类型判断对象
class Animal(object):
	def __init__(self):
		self.x = 10
#判断一个变量是否是某些类型中的一种
if __name__ == '__main__':
	print(isinstance(Animal(),Animal))
	print(isinstance([1,2,3,4,5],(list,tuple)))
	#获取对象的所有属性和方法
	print(dir(str))
	print('hello'.__len__())
	#判断属性是否存在
	print(hasattr(Animal(), 'x'))
	#获取属性
	print(getattr(Animal(),'x'))

#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student(object):
	count = 0
	def __init__(self,name):

		self.name=name
		Student.count+=1

		
# 测试:
if Student.count != 0:
    print('测试失败0!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败1!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败2!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
