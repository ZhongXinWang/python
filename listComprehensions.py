#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import os
print("-----------------列表生成式的学习-----------------");
#生成一个x*x的列表
L = [];
for x in range(1,10):
	L.append(x*x)
print(L);
#使用列表生成式
lc = [x*x for x in range(1,10)];
print(lc)
#只取奇数的数
lj = [x for x in range(1,10) if(x % 2 !=0)]
print(lj)
#生成tuple
T = [(k,v) for k,v in {"key1":"1","key2":"2"}.items()]
print(T);
#把list的字符串变成小写
print([v.lower() for v in ['Hello', 'World', 'IBM', 'Apple']])

#列出当前文件夹下面的所有文件
#print(help(os.listdir))
print([d for d in os.listdir()])

#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L1 = ['Hello', 'World', 18, 'Apple', None]
print([v.lower() for v in L1 if (isinstance(v,str))])