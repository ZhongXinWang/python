#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
import jieba
from scipy.misc import imread  # 这是一个处理图像的函数，读取图像
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  #词云生成库
import matplotlib.pyplot as plt  #绘制库

back_color = imread('C:/Users/wzx/Desktop/word.jpg')  # 解析该图片
 # 使用内置的屏蔽词，再添加'损害'
STOPWORDS.add('《共·惨党宣言》')
#设置字体
font = 'C:/Windows/Fonts/simhei.ttf'
wc = WordCloud(background_color='white',  # 背景颜色
               max_words=1000,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=80,  # 显示字体的最大值
               stopwords=STOPWORDS, 
               font_path=font,  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               )
# WordCloud各含义参数请点击 wordcloud参数

# 添加自己的词库分词，比如添加'中国改革开放'到jieba词库后，当你处理的文本中含有中国改革开放这个词不会拆，
jieba.add_word('中国改革开放')

# 打开词源的文本文件
with open('cnword.txt','r',encoding="utf-8") as f:
	text = f.read()
#print(text)
# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('stopwords.txt','r',encoding="utf-8") as f:#utf-8格式读取文件
        str_text = f.read()
        f.close()  # stopwords文本中词的格式是'一词一行'
    for word in word_generator:
        if word.strip() not in str_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格


text = stop_words(text)
#print(text)
wc.generate(text)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('new3.png')