#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
print('-------高级特性------------')
#__slots__限制对象属性被调用
class Person(object):
	#设置运行被对象直接访问的属性
	__slots__=('name','age')
	def __init__(self,name,age):
		self.name=name
		self.age = age
	def toString(self):
		return self.name,self.age

print('-----------------开始封装提供get和set方法-------------------')
class Animal(object):
	def __init__(self,name):
		self.__name = name
	def setName(self,name):
		self.__name = name
	def getName(self):
		return self.__name
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
	#只读属性
	@property
	def resolution(self):
		return self._width*self._height
	@property
	def width(self):
		return self._width
	#读写
	@width.setter
	def width(self,value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
		self._height = value
	
if __name__ == '__main__':

	p = Person('王五',90);
	p.name = '李四'
	#没有被允许的属性不能直接使用，否则报错AttributeError
	#p.age = 100
	print(p.toString())
	a = Animal('hello');
	#私有属性无法被修改
	a.__name='ddd'
	print(a.getName())
	# 测试:
	s = Screen()
	s.width = 1024
	s.height = 768
	print('resolution =', s.resolution)
	if s.resolution == 786432:
		print('测试通过!')
	else:
		print('测试失败!')

