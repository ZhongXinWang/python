#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
from io import StringIO
from io import BytesIO
'''
	把str写到内存中的StringIO
	把字节写道内存中的BytesIO
'''
#写
f = StringIO('Hello\nWorld\n')
print(f.getvalue())
#读
while True:
	s = f.readline()
	if (s == ''):
		break;
	print(s.strip())

fb = BytesIO()
fb.write('中文'.encode('utf-8'))
print(fb.getvalue())