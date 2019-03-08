#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import threading
#print(dir(threading))
thread_local = threading.local()
def process_student():
	std = thread_local.student
	print('Hello,%s(in %s)' % (std,threading.current_thread().name))
def add_local(name):
	thread_local.student = name
	process_student()
t1 = threading.Thread(target=add_local,args=('Winston',),name='Thread1')
t2 = threading.Thread(target=add_local,args=('gerald',),name='Thread2')
t1.start()
t2.start()
t1.join()
t2.join()