#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang

print("---------------切片功能开始-------------")
L = []


for i in range(1,10):
	L.append(i)

print(L)
#使用slice获取前三个元素
print(L[0:3])
print(L[:3])
#使用slice获取后三个元素
print(L[-3:])
#取奇数从第0个数开始到第9个数，每两个取一个
print(L[0:9:2])
#tupel做切片
T = (1,3,4,5,6)
print(T[3:])
#字符串做切片
str = "helloWorld"
print(str[-5:])

#使用slice实现字符串去除空格
def trim(s):
	#去左边
	if(s[:1] == " "):

		return trim(s[1:])
	#去右边
	if(s[-1:] == " "):

		return trim(s[:-1])
	return s


if trim('hello  ') != 'hello':
    print('测试失败1')
elif trim('  hello') != 'hello':
    print('测试失败2')
elif trim('  hello  ') != 'hello':
    print('测试失败3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4')
elif trim('') != '':
    print('测试失败5')
elif trim('    ') != '':
    print('测试失败6')
else:
    print('测试成功!')