#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import sqlite3
print(dir(sqlite3.Connection))
#创建连接
conn = sqlite3.Connection('test.db')
#创建表
try:
	conn.execute('create table test(id int primary key not null,name text)');
except sqlite3.OperationalError as e:
	pass
#插入数据
insert_sql = 'insert into test (id,name) values(?,?)';
conn.execute(insert_sql,('1','张三'))
conn.execute(insert_sql,('2','李四'))
#查询
select_sql = 'select *from test';
cursors = conn.execute(select_sql)
for row in cursors:
	print('id=%s-->name=%s' % (row[0],row[1]))
conn.close()