#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
#定义一个list
print('---------------list有序列表--------------')
list = [1,2,3,4,5,6]
print(list)
#foreach输出
for item in list:
	print(item);
#while循环
print('----------------while循环---------------')
i = 0;
while(i < len(list)):
	print(list[i])
	i+=1;
print('---------数组越界异常捕获-------')
try:
	print(list[10])
except IndexError as e:
		print('数组越界')
print('---------逆索引取元素-------')

print('最后一个元素：',list[-1])
print('-----------------添加元素----------')
#末尾追加
list.append('tail');
#指定位置添加
list.insert(2,'指定位置插入元素')
print(list)
print('----------------从尾巴取出元素与删除----------')
#尾巴出队
value = list.pop();

#删除指定位置元素
list.pop(2)
print(list)

print('-------------------tuple元组，一旦初始化不能修改--------------')
#定义
tuple = ('张三','李四','王五');
for item in tuple:
	print(item);
#元组没有insert，pop方法
#定义空的
tuple1 = ()
#定义只有一个元素
tuple2 = (1,)

print(tuple2.count(1))
print(len(tuple2))
print(dir(tuple2))

#例子
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])