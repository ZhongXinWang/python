#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
from collections import Iterable
print("---------使用生成器替换列表生成式节约空间----------");
#列表生成式
print([v  for v in range(10)])
#[]替换为()变成生成器
g = (v for v in range(10));
print(g)
#获取生成器的值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#判断generator是否式可迭代
if(isinstance(g,Iterable)):
	for i in g:
		print(i);
print('---------斐波那契数列----------')
#生成斐波那契数列
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b);
		a,b = b,a+b 
		'''
		t = (b, a + b) # t是一个tuple
		a = t[0]
		b = t[1]
		'''
		n = n+1;
	return 'done'
fib(3)

#修改为generator,添加yield就表示是一个generator
def fibG(max):
	n,a,b = 0,0,1
	while(n < max):
		yield b
		a,b = b,a+b
		n = n+1;
	return "done"
#调用
o = fibG(3)
print(next(o))
print(next(o))
print(next(o))

#测试yield
def testYield():
	print('step 1');
	yield 1;
	print('step 2');
	yield 2;
	print('step 3');
	yield 3;
y = testYield();
for i in y:
	print(i)
#输出杨辉三角
print('----------------输出杨辉三角---------------')
def triangles():
	
	L1 = [1]
	n = len(L1)
	while True:
		yield L1
		l = [1]
		#取第一个数加上第二个
		i = 0;
		while i+1 != n:
			l.append(L1[i]+L1[i+1])
			i = i + 1
		#取第二个数加上第三个
		l.append(1)
		L1= l
		n = len(L1)
	return 'done'

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')