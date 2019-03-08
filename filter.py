#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
print('-------------Python内建的filter()函数用于过滤序列学习-------------')
'''
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素
'''
L = list(range(1,100));
#保留奇数，使用map并不能把不需要的元素给移除，只会返回None.L的长度不变
def odd(value):
	if(value % 2 != 0):
		return value;

for i in map(odd,L):
	print(i);
#使用filter来过滤，返回true和false
def oddFilter(value):
	if(value % 2 != 0):
		return True;
	return False
#list的长度被重新构建，只把满足条件的元素放到list中	
for i in filter(oddFilter,L):
	print(i);
'''
 计算素数的一个方法是埃氏筛法，
 (1）先把1删除（现今数学界1既不是质数也不是合数
（2）读取队列中当前最小的数2，然后把2的倍数删去
（3）读取队列中当前最小的数3，然后把3的倍数删去
（4）读取队列中当前最小的数5，然后把5的倍数删去
（5）读取队列中当前最小的数7，然后把7的倍数删去
（6）如上所述直到需求的范围内所有的数均删除或读取
'''
#埃氏筛法求100以内的素数
#定义一个序列生成器,生成3以上的自然数
def oddIter():
	n = 1;
	while True:
		n = n+2
		yield n
#定义一个筛选函数
def notDivisible(n):
	#不能整除他的数返回
	return lambda x:x%n>0
#定义一个素数生成器
def primes():
	yield 2
	it = oddIter()
	while True:
		n = next(it)
		yield n
		#构建新序列,旧it，notDivisible
		it = filter(notDivisible(n),it)
# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
#筛选出回数
def is_palindrome(n):

	'''
	(len(s)//2)表示整除
	n = 12321
	s = str(n) 转化为str使用切片
	s[:(len(s)//2)+1]  123
	s[(-(len(s)//2))-1:]  321  使用[::-1]让字符串反向
	第一个:表示开始位置,第二个结束位置:,第三个从末端开始取
	'''
	s = str(n)
	return s[:(len(s)//2)+1] == s[(-(len(s)//2)-1):][::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')