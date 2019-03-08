#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
'''
打开网页 get()
find_element_by_css_selector()  根据选择器找元素
find_elements_by_tag_name() 根据标签的名字
execute_script() 执行脚本
set_page_load_timeout() #等待超时时间
'''
#指定浏览器的位置
'''
会启动浏览器
browers = webdriver.Chrome()
browers.set_page_load_timeout(30)
print(dir(browers))
'''
#无头浏览器模式
chrome_options = Options()
chrome_options.add_argument('--headless')
browers = webdriver.Chrome(chrome_options=chrome_options)
browers.set_page_load_timeout(30)
#打开浏览器
browers.get('http://www.17huo.com/newsearch/?k=%E5%86%85%E8%A3%A4')
#获取数据
#点击分页，获取下一页的数据
for i in range(3):
	print('--------------第%s页-------------' % (i+1))
	browers.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	goods = browers.find_element_by_css_selector('#book_item_list').find_elements_by_css_selector('.book_item_list_box')
	for good in goods:
		name = good.find_element_by_css_selector('div.shop_box > div.book_item_mid.clearfix > a').text;
		price = good.find_element_by_css_selector('div.shop_box > div.book_item_mid.clearfix > div.book_item_price > span').text;
		print('商品名称：%s,商品价格：%s' % (name,price))
	nextPage = browers.find_element_by_css_selector('body > div.wrap > div.search_container > div.main_new > div.tcdPageCode.goldPage > a.nextPage');
	nextPage.click()
	time.sleep(5)





