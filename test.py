#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
from datetime import datetime
import time,re,logging
from collections import Iterable
'''
获取这个月的所有工作日期

'''
#获取填写日报的日期，规则：把当月所有的工作日时间全部返回
def getDateByTime(date):
	workDate=[]
	#自定义月份
	if(date != None and len(date) > 0):
		t = re.split(r'(\d{4}-\d{1,2}-)',date)[1]
	else:
		t = str(time.strftime('%Y-%m-'))
	for i in range(1,32):
		#拼接成2018-10-1
		timeStr=t+str(i)
		try:
			tmp = time.strptime(timeStr,'%Y-%m-%d')
			 #判断是否为周六、周日
			if (tmp.tm_wday !=6) and (tmp.tm_wday!=5):
				workDate.append(time.strftime('%Y-%m-%d',tmp))
		except:
			print('日期越界')
	if len(workDate)==0:
		workDate.append(time.strftime('%Y-%m-%d'))
	return workDate

#print(getDateByTime('2018-11-09'))

L = [1,2]
L = L[1:]
#print(L)

#print(re.match(r'^工作日志流程.*','工作日志流程申请-Winston（王钟鑫）-开发一部 Development Dept. I-2018-10-09'))
#print('2018-10'>'2018-10')
def compareTo(strs):
	d = datetime.strptime(strs,'%Y-%m-%d %H:%M')
	sinoDate = str(d.year)+"-"+str(d.month)

	#currentMonth = str(datetime.now().year)+"-"+str(datetime.now().month)
	currentMonth = "2018-10"
	
	if(currentMonth == sinoDate):
		return 1
	elif(sinoDate[-2:] > currentMonth[-2:]):
		return 2
	else:
		return 0
dates = ['2018-10-11 11:00','2018-10-11 12:00','2018-11-11 12:00',
'2018-09-11 12:00','2018-09-15 12:00']
i = 0
L1 = []
n = 5
j = 0
while True:
	for x in dates:
		flag = compareTo(x)
		if( flag== 0):
			i = 1
			break;
		elif(flag == 2):
			continue;
		L1.append(x)
	print(i)
	if(i == 1):
		break;
	j = j+1
#print(L1)
def writeFile(fileName,L):
	if(isinstance(L,Iterable) == True):
		with open(fileName, 'w+', encoding = 'utf-8') as f:
			for l in L:
				f.write(l)
	else:
		logging.error('传入的Iterable对象')

L = []
L.append('2018-19-25'+'hahhahhahaaa\n')
L.append('2018-19-24'+'hahhahhahaaa\n')
sortedL = sorted(L)
#writeFile('hello.txt','ffdfdf')
logging.info('dd')