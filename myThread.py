#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import time,threading
# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
#获取当前线程名字
print(threading.current_thread().name)
#创建一个新的线程
t = threading.Thread(target=loop,name='loopThread')
#启动
t.start();
t.join();
print('thread %s ended.' % threading.current_thread().name)
print(dir(threading))