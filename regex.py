#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import re
from datetime import datetime, timezone, timedelta
#匹配电话号码
def matchs(match,value):
	if(re.match(match,value) != None):
		print('正确')
	else:
		print('匹配失败')
matchs(r'^\d{3}\-\d{3,8}$','123-22117')
matchs(r'^\d{3}\-\d{3,8}$','123 908979')
#匹配手机号
matchs(r'^[1]\d{10}$','15759075920')
#匹配身份证
matchs(r'\d{17}[\d|xX]{1}$','35062419941205051x')

#切分字符串
print(re.split(r'\s+','a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.match(r'^[工作日志流程].*','工作日志流程-Winston（王钟鑫）-开发一部'))
def compareTo(strs):
	d = datetime.strptime(strs,'%Y-%m-%d %H:%M')
	current = str(d.year)+"-"+str(d.month)
	now = str(datetime.now().year)+"-"+str(datetime.now().month)
	if(current == now):
		return True
	return False
print(compareTo('2018-11-30 09:04'))



