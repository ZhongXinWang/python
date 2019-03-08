#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
print('------------返回函数------------------')
'''
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的
'''
#可变参数调用的时候需要用*
def sumCalc(*args):
	ax = 0;
	for item in args:
		ax=ax+item
	return ax
L = list(range(1,100))
print(sumCalc(*L))
#不想马上得到返回的结果，可以返回一个函数
#内部函数可以调用外部函数的局部变量
def lazySum(*args):
	def sumCalc():
		ax = 0;
		for item in args:
			ax=ax+item
		return ax
	return sumCalc

fun = lazySum(*L)
print(fun())

#利用闭包返回一个计数器函数，每次调用它返回递增整数
#nonlocal声明在闭包中，可以使用不再该函数内的变量可以被修改
def createCounter():
	i = 0
	def counter():
		nonlocal i
		i+=1
		return i

	return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())

#使用lambda函数,过滤掉所有的整数，使用匿名函数，：前面的是参数，后面是逻辑
L1 = list(filter(lambda n:n % 2 == 1, range(1, 20)))
print(L1)