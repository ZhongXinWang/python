#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
print('--------------------继承----------------------')
#定义一个Aniaml类
class Animal(object):
	def run(self):
		print('Animal 动物类')

#定义Dog类继承自Animal
class Dog(Animal):
	def run(self):
		print('Dog run.....')
#定义Cat类
class Cat(Animal):
	def run(self):
		print('Cat run......')

def runAnimal(animal):
	animal.run();

if __name__=='__main__':
	#使用多态
	runAnimal(Dog())
	dog = Dog()
	# True
	print(isinstance(dog,Animal))
	#False,animal不是一种狗
	print(isinstance(Animal(),Dog))

