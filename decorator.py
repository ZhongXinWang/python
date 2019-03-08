#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import functools,time
print('---------------开始装饰者模式-------------------')
#获取函数的名字,每个函数都有的属性
def now():
	return  "2018-10-21"
print(now.__name__)
#装饰者添加日志
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		print(args)
		return func(*args,**kw)
	return wrapper
#添加注解,使用decorator
@log
def decoratorLog(L):
	return '2018-10-21'
print(decoratorLog([1,2,3,4]))

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		start = time.time()
		rs = func(*args,**kw)
		end = time.time()
		print('%s executed in %s ms' % (func.__name__, end-start))
		return rs
	return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')