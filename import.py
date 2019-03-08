#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import sys
print('-----------第三方模块的使用--------------')
print(dir(sys))
def test():
	print(sys.argv)
#如果该函数没有被调用，就会执行if里面的东西
if __name__=='__main__':
	test()