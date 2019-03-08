#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import requests
from bs4 import BeautifulSoup
print(dir(BeautifulSoup))
url = 'http://www.baidu.com';
with requests.get(url) as r:
	r.encoding='utf-8'
	soup = BeautifulSoup(r.text)
	#格式化
	pret = soup.prettify();
	u = soup.select('#u1 a')
	for i in u:
		print("名称：%s,地址:%s" % (i.getText(),i.get('href')))