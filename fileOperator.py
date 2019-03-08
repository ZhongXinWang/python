#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import logging
#打开一份文件,如果找不到会抛异常
def openFile(fileName,types):
	try:
		handle = open(fileName,types,encoding='utf-8')
		#把内容读取到内存中
		return handle.read()
	except FileNotFoundError as e:
		logging.error(e)
	finally:
		if handle:
			handle.close()
def writeFile(fileName,types,content):
	with open(fileName,types,encoding='utf-8') as f:
		f.write(content)

if __name__ == "__main__":
	content = openFile('filter.py','r');
	logging.error(content)
	writeFile('testWrite.py','w','''{
    "code":100,
    "data":[
        1,
        2,
        3,
        4,
        5,
        6
    ]
}''')

