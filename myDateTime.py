#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import re,time
from datetime import datetime, timezone, timedelta
'''
python的第三方日期模块
'''
print(dir(datetime))
#获取当前时间
print(datetime.now())
#从当前时间获取到对应的时间
print(datetime.time(datetime.now()))
#一个datetime类型转换为timestamp
print(datetime.timestamp(datetime.now()))
#str转换为datetime
print(type(datetime.strptime('2018-10-27','%Y-%m-%d')))
#datetime转化为str
print(type(datetime.strftime(datetime.now(),'%Y-%m-%d')))

#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
#以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
def to_timestamp(dt_str, tz_str):
    #把获取的时间转化为datetime，并设置时区
    date = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz = (re.split(':',re.split(r'^UTC',tz_str)[1])[0]);
    print(tz)
    tz_utc = timezone(timedelta(hours=int(tz)))
    dt = date.replace(tzinfo=tz_utc)
    return dt.timestamp()
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0,t2
print('ok')


#获取填写日报的日期，规则：把当月所有的工作日时间全部返回，2018-11-09,返回list
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
def getDateByTimeReturnDic(date):
	workDate={}
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
				workDate[time.strftime('%Y-%m-%d',tmp)] = time.strftime('%Y-%m-%d',tmp)
		except:
			print('日期越界')
	if len(workDate)==0:
		workDate[time.strftime('%Y-%m-%d')] = time.strftime('%Y-%m-%d')
	return workDate

dicWork  = getDateByTimeReturnDic('2018-11-09')
L = ['2018-11-02','2018-11-03','2018-11-04','2018-11-05']
noWrite = [] 
for l in L:
	if(dicWork.__contains__(l) == False):
		noWrite.append(l)

print(noWrite)


