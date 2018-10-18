# -*- coding: utf-8 -*-
#切片
L = list(range(1,20))
print(L)
#获取0-3的元素值,[1, 2, 3]
print(L[0:3])
#从尾巴取-1是最后一个
print(L[-1])

##########匿名函数###########
def is_odd(n):
    return n % 2 == 1
#不使用匿名函数
rs = list(filter(is_odd, range(1, 20)))
#验证匿名函数
rs = list(filter(lambda x:x%2==1,range(1,20)))
print(rs)
