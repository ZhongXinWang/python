#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
from collections import Iterable
print("------------开始使用for循环-------------");
#普通for  in 循环
L = [];
for i in range(100):
	L.append(i);

#判断对象是否可迭代
print(isinstance(L,Iterable))
print(isinstance(333,Iterable))

#返回下标的迭代
for i,value in enumerate(L):
	print("i=",i,"value=",value);

#迭代tuple
for x,y in [(1,1),(2,2),(3,3)]:
	print(x,y)

#返回一个list中最小和最大值,返回一个tuple
def findMinAndMax(list):
	if(list == []):
		return (None,None);
	list.sort();
	return (list[:1][0],list[-1:][0])

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4')
else:
    print('测试成功!')