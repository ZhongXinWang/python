#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import time,threading
#定义全局变量
balance=0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
    #print(threading.current_thread().name,'=>',balance)
def run_thread(n):
	for i in range(100000):
		#修改的时候获得锁
		lock.acquire()
		try:
			change_it(i)
		finally:
			#改完释放
			lock.release()
#定义两个线程
t1 = threading.Thread(target=run_thread,name='Thread1',args=(5,))
t2 = threading.Thread(target=run_thread,name='Thread2',args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)