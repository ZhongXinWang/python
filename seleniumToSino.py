#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import time,re,logging
from selenium import webdriver
from collections import Iterable
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timezone, timedelta

browers = webdriver.Chrome()
browers.set_page_load_timeout(30)
url_login = 'http://oa.sinoservices.com/seeyon/main.do?method=login'
url_send = 'http://oa.sinoservices.com/seeyon/collaboration/collaboration.do?method=listSent&_resourceCode=F01_lis'
url_detail = 'http://oa.sinoservices.com/seeyon/collaboration/collaboration.do?method=summary&openFrom=listSent&affairId='
#设置无头浏览器
'''chrome_options = Options()
chrome_options.add_argument('--headless')'''
browers = webdriver.Chrome(chrome_options=chrome_options)
browers.set_page_load_timeout(30)
#写入文件的方法类
def writeFile(fileName,L):
	if(isinstance(L,Iterable) == True):
		with open(fileName, 'w+', encoding = 'utf-8') as f:
			for l in L:
				f.write(l)
	else:
		logging.error('传入的Iterable对象')
#只找在当前月份内的id
def compareTo(strs):
	d = datetime.strptime(strs,'%Y-%m-%d %H:%M')
	sinoDate = str(d.year)+"-"+str(d.month)
	#获取当前月
	currentMonth = str(datetime.now().year)+"-"+str(datetime.now().month)
	#currentMonth = "2018-10",也可直接写死
	#找到和当前月份相等的
	if(currentMonth == sinoDate):
		return 1
	#如果比当前月份大，则跳过
	elif(sinoDate[-2:] > currentMonth[-2:]):
		return 2
	else:
		return 0
#登录系统
def login(uname,passwd):
	browers.get(url_login)
	input_name = browers.find_element_by_xpath('//*[@id="login_username"]')
	input_passwd = browers.find_element_by_xpath('//*[@id="login_password"]')
	submit = browers.find_element_by_xpath('//*[@id="login_button"]')
	input_name.send_keys(uname)
	input_passwd.send_keys(passwd)
	submit.click()
	time.sleep(5)
#获取已经发送界面的数据
def getSend():
	browers.get(url_send)
	time.sleep(5)
	L = []
	i = 0
	try:
		while True:
			rows = browers.find_element_by_css_selector('#listSent').find_elements_by_tag_name('tr')
			for row in rows:
				name = row.find_element_by_css_selector('td:nth-child(2) > div > span.grid_black').text
				startDate = row.find_element_by_css_selector('td:nth-child(3) > div').text
				track = row.find_element_by_css_selector('td:nth-child(6) > div > a')
				flag = compareTo(startDate)
				if( flag== 0):
					i = 1
					break
				elif(flag == 2):
					continue
				if(re.match(r'^工作日志流程.*',name)):
					L.append(track.get_attribute('affairid'))
			#如果i == 1表示没有必要下一页了，否则点击第二页
			if(i == 1):
				break
			#寻找下一页
			nextPage = browers.find_element_by_css_selector('div.pDiv2.common_over_page.align_right > a.pNext.pButton.common_over_page_btn')
			nextPage.click()
			time.sleep(5)
	except Exception as e:
		logging.error(e.message)
	return L
#获取日志详情内的所有内容
def getDetail(L):
	s = set()
	ws = []
	for item in L:
		
		try:#打开地址
			browers.get(url_detail+item)
			time.sleep(5)
			#切换iframe
			browers.switch_to_frame('componentDiv')
			browers.switch_to_frame('zwIframe')  
			rows = browers.find_element_by_css_selector('#formson_1598').find_elements_by_tag_name('tr')
			rows = rows[1:]
			for row in rows:
				startDate = row.find_element_by_css_selector('#field0009').text
				detail = row.find_element_by_css_selector('#field0021_span').text
				s.add(startDate)
				ws.append('日志时间:'+startDate+"----日志内容:"+detail+"\n")
		except Exception as e:
			logging.error(e.message)
	#写到文件中去
	sortedL = sorted(ws)
	writeFile('detail.txt',sortedL)
	return s

#获取填写日报的日期，规则：把当月所有的工作日时间全部返回自定义：2018-11-09
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
			logging.error('日期越界')
	if len(workDate)==0:
		workDate[time.strftime('%Y-%m-%d')] = time.strftime('%Y-%m-%d')
	return workDate
#页面获取的月份和工作日的比对
def check(pageDate,workDate):
	noWrite = []
	for item in pageDate:
		#没包含该日期表示没写
		if(workDate.__contains__(item) == False):
			noWrite.append(item)
			#写到文件中去
	sortedL = sorted(noWrite)
	writeFile('noWrite.txt',sortedL)
	
if __name__=='__main__':
	#登录系统
	login('Winston.Wang','wzx199412')
	#获得指定月份的所有id
	sendIds = getSend()
	#获取日志详情内的所有内容
	details = getDetail(sendIds)
	#返回指定月或是默认当前月的工作日，返回dic
	workDateDic = getDateByTimeReturnDic('2019-03-01')
	#页面获取的月份和工作日的比对
	check(details,workDateDic)
	#关闭浏览器
	browers.close()

