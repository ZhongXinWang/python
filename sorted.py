#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
print('--------------python的内置排序方法--------------')
L = [100,2,35,-22,4,-5,786,43]
sortedL = sorted(L)
#默认升序
print(sortedL)
#降序
print(sorted(L,reverse=True))
#指定函数，按绝对值大小
print(sorted(L,key=abs,reverse=True))
#排序字符串,升序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#排序字符串,升序并把所有的字母转化为小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#对tuple进行排序，按名字排序
L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
#key指定的方法只是让内置的函数知道我们是要那第几个属性去排序的
L2 = sorted(L1, key=by_name)
print(L2)