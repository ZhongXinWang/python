#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang

print('开始dic字典练习')
#定义字典，类似javamap
D = {'Michael':95,'Bob':100,'Winsotn':100}
#获取某个值
print(D['Winsotn'])
print('---------遍历方式1')
#遍历key
for item in D:
	print(item)

print('---------遍历方式2')
#遍历value
for item in D.values():
	print(item)
print('---------遍历方式3')
#修改值，判断key是否存在
if 'Michael' in D:
	D['Michael'] = 99


#遍历key取value
for item in D:
	print(D[item])

print('开始set练习')
#定义一个set
s = set([1,2,3,4,4])

#添加元素
s.add(5)

print(s)
