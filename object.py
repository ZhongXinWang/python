#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
print('---------------面向对象------------------')
class Person(object):
	def __init__(self,name,score):
		self.name=name
		self.__score = score
	def toString(self):
		return self.name,":",self.__score
	def setScore(self,score):
		self.__score = score
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def getGender(self):
    	return self.__gender
    def setGender(self,gender):
    	self.__gender = gender
if __name__ == '__main__':
	p = Person('张三',90)
	print(p.toString())
	p.name='修改为李四'
	#变量已经被设置为私有，p.__score=40无法修改，两个_
	p.setScore(40)
	print(p.toString())
	# 测试:
	bart = Student('Bart', 'male')
	if bart.getGender() != 'male':
   		print('测试失败!')
	else:
   		bart.setGender('female')
	if bart.getGender() != 'female':
   		print('测试失败!')
	else:
		print('测试成功!')





