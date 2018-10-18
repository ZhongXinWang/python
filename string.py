#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''获取字符的unicode编码'''
print('unicode编码=',ord('中'))
'''把编码转为字符'''
print('转码:%s' % (chr(20013)))

#把str转化为byte
print('中文'.encode('utf-8'))
#把byte转化为str
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#忽略错误
print(b'\xe4\xb8\xad'.decode('utf-8',errors='ignore'))
#获取字符串长度
print('len=',len('中文'))
#计算字节长度
print('lenByte=',len('中文'.encode('UTF-8')))
#保留小数
print('%.2f' % 3.1415926)