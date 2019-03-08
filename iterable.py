#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
#引入包
from collections import Iterable
from collections import Iterator
print('---------------迭代器----------------')
#判断是否是可以迭代的,Iterable对象
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance(1234,Iterable))
#生成器是一个Iterator迭代器，还可用next()
print(isinstance((x for x in range(10)),Iterator))
print(isinstance({},Iterator))

#把list、dict、str等Iterable变成Iterator可以使用iter()函数
it = iter('hello')
print(next(it))