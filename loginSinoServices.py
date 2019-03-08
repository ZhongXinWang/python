#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import requests
from bs4 import BeautifulSoup
import html5lib
import re
import time,json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
s = requests.Session()
url_login = 'http://oa.sinoservices.com/seeyon/main.do?method=login'
url_send = 'http://oa.sinoservices.com/seeyon/collaboration/collaboration.do?method=listSent&_resourceCode=F01_lis'
url_detail = 'http://oa.sinoservices.com/seeyon/collaboration/collaboration.do?method=summary&openFrom=listSent&affairId='
formdata = {
    'login_username': 'Winston.Wang',
    'login_password': 'wzx19941205'
}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
r = s.post(url_login,data = formdata, headers = headers)
if(r.status_code == 200):
	time.sleep(3)
	send = s.get(url_send)
	try:
		bsObj = BeautifulSoup(send.text)
		with open('sino.html', 'w+', encoding = 'utf-8') as f:
			f.write(send.text)
	except Exception as e:
		print(e)

