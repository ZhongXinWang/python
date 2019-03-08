#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import logging
def div(s):
	return 10/int(s);
def foo(s):
	print(div(s));
if __name__ == '__main__':
	try:
		foo(0)
	except ZeroDivisionError as e:
		logging.error(e)
	finally:
		logging.debug('程序执行结束')
