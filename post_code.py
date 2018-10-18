import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate
###########start############
class DefaultSaxHandler(object):
        def __init__(self,provinces):
                self.provinces = provinces
     #开始解析
        def start_element(self,name,attrs):
                if name != 'map':
                        name = attrs['title']
                        number = attrs['href']
                        self.provinces.append((name,number))
     #结束节点就跳过
        def end_element(self,name):
                pass
        
        def char_data(self,text):
                pass
    
def get_province_entry(url):
    content = requests.get(url).content.decode('gb2312')
    print(content)
    #开始位置,返回这个节点的开始位置在第几行
    start = content.find('<map name=\"map_86\" id=\"map_86\">')
    #结束位置在第几行
    end = content.find('</map>')
    print(start,end)
    #使用切片
    content = content[start:end + len('</map>')].strip()
    provinces = []
    #获得对象
    handler = DefaultSaxHandler(provinces)
    #创建解析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(content)
    return provinces
provinces = get_province_entry('http://www.ip138.com/post/')
print(provinces)
