#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import json
'''
json在python中的使用

'''
L = [1,2,3,4,5,6];
dic = {"name":"张三","age":40}
print(dic.get('name'))
jsonStr = json.dumps(dic)
print(json.dumps(jsonStr))
print(json.dumps(L))
#解析json
jObject = json.loads(jsonStr)
print(jObject)

#从文件读取json，并解析
with open('testWrite.py','r',encoding='utf-8') as f:
	content = f.read()
	parse = json.loads(content)
	print(parse.get('code'),parse.get('data'))