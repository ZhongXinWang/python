#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
from functools import reduce
print("---------------开始map之旅-------------")
'''
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，
并把结果作为新的Iterator返回
我们有一个函数f(x)=x2，
把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，
就可以用map()实现如下
'''

def m2(x):
	return x*x;
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#可以将获取到的数据作为一个list，定义一个解析的函数进行解析
for x in map(m2,L):
	print(x);
#把这个list所有数字转为字符串
print(list(map(str,L)));
'''
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
#求和
def sum(x,y):

	return x+y;
reduceL = list(range(1,100))
print(reduce(sum,reduceL))
# 把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def change(x,y):
	return x*10+y;
print(reduce(change,[1, 3, 5, 7, 9]))

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']：
'''

def normalize(name):
	return name.lower().capitalize();
print(list(map(normalize,['adam', 'LISA', 'barT'])))