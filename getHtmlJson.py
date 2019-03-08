#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
from bs4 import BeautifulSoup
import json,re
htmlfile = open('sino.html','r',encoding='utf-8')
read = htmlfile.read()
#findword = u"(\$\.ctx\.fillmaps = {)(.*)(}};)"
findword = u"({\"listSent\")(.*)(}};)"
pattern = re.compile(findword)
results = pattern.findall(read)
t = results[0]
s = ""
for i in t:
	s = s+i
s = s[:-1]
JsonObject = json.loads(s)
jsonData = JsonObject.get("listSent").get("data");
for i in jsonData:
	if(i.get('subject').startswith('工作日志流程')):
		print(i.get('subject'),i.get('startDate'))